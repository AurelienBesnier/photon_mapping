import random
import sys
import time

from openalea.plantgl.all import * 
from openalea.lpy import Lsystem
import matplotlib.pyplot as plt

from photonmap import libphotonmap_core
from photonmap import (
    Vec3,
    PhotonMapping,
    UniformSampler,
)

from photonmap.libphotonmap_core import (
    Render,
    visualizePhotonMap,
    visualizeCaptorsPhotonMap,
)

from photonmap.Reader import (ReadRADGeo, ReadPO)
from photonmap.Energy import (CalculateEnergy, CorrectEnergy)
from photonmap.Loader import (LoadCaptor, LoadEnvironment, LoadPlant)
from photonmap.Common import (Outils)



class Simulator:
    """
    A class which include all the tools of simulation.

    Attributes
    ----------
    nb_photons: int
        The number of photons in simulation
    maximum_depth: int
        The maximum number of times that the light bounces in the scene 
    scale_factor: float
        The size of geometries. The vertices of geometries is recalculated by dividing their coordinates by this value
    t_min: float
        The minimum distance between the point of intersection and the origin of the light ray
    nb_thread: int
        The number of threads on the CPU used to calculate in parallel. This value is between 0 and the number of cores of your CPU.
    is_backface_culling: bool
        Define which mode of intersection is chosen: intersect only with the front face or intersect with both faces.
    base_spectral_range: dict
        The base spectral range which includes all the other spectral ranges
    divided_spectral_range: array
        The list of spectral ranges divided from the base spectral range.
    rendering: bool
        Set to True to render the output images
    N_sim_captor: dict
        Number of received photons in each captor
    N_sim_plant: dict
        Number of received photons in each organ of plant

    captor_file: str
        The link to the file which contains the informations of the captors in the simulation
    spectrum_file: str
        The link to the file which contains the informations of the heterogeneity of the spectrum
    points_calibration_file: str
        The link to the file which contains the informations of the captors used to calibrate the final result 

    plant_file: str
        The link to the file of the model of plant. (currently only support .lpy file)
    plantPos: Vec3
        The position of the plant

    po_dir: str
        The link to the folder which contains the optical properties of the room
    
    """
    #constructor
    def __init__(self):
        self.nb_photons = 0
        self.max_depth = 0
        self.scale_factor = 1
        self.t_min = 0
        self.nb_thread = 8
        self.is_backface_culling = False
        self.base_spectral_range = {"start": 0, "end": 0}
        self.divided_spectral_range = []
        self.rendering = False
        #
        self.captor_file = ""
        self.plant_file = ""
        self.po_dir = ""
        

    def run(self):
        """
        Run the simulation with the configurations which is determined

        Returns
        -------
            The number of received photons on each captor and organs of plant is saved into the files located in folde ./results 

        """

        scene = libphotonmap_core.Scene()
        n_estimation_global = 100
        final_gathering_depth = 0 

        self.N_sim_captor = []
        self.N_sim_plant = []

        for index in range(len(self.divided_spectral_range)):
            start_time = time.time()
            current_band = self.divided_spectral_range[index]
            
            print("Wavelength:", current_band["start"], "-", current_band["end"])
            moyenne_wavelength = (current_band["start"] + current_band["end"]) / 2
            scene.clear()
            scene, has_captor, captor_triangle_dict, has_plant, tr2shmap = self.initSimulationScene(scene, current_band, moyenne_wavelength)
            
            #create integrator
            scene.tnear = self.t_min
            scene.setupTriangles()
            scene.build(self.is_backface_culling)

            integrator = PhotonMapping(
                self.nb_photons,
                n_estimation_global,
                final_gathering_depth,
                self.max_depth,
                self.nb_thread
            )

            print("Build photonMap...")
            
            sampler = UniformSampler(random.randint(1, sys.maxsize))
            
            # build no kdtree if not rendering
            integrator.build(scene, sampler, self.rendering)
            print("Done!")
            
            #rendering if declared
            if(self.rendering):
                self.render(integrator, scene, moyenne_wavelength, sampler)


            #read energy of captor/plant
            captor_energy = {}
            if(has_captor):
                CalculateEnergy.captor_add_energy(captor_triangle_dict, integrator, captor_energy)
                self.N_sim_captor.append(captor_energy)
                

            #Plant Energie
            plant_energy = {}
            if(has_plant):
                plant_energy = CalculateEnergy.plant_add_energy(tr2shmap, integrator)
                self.N_sim_plant.append(plant_energy)
            
            print("Time taken: " + str(time.time() - start_time))


        if len(self.N_sim_captor) > 0:
            N_mes_captor = []
            if self.spectrum_file != "":
                # Setting up spectrum bands to correct energy
                integrals = CorrectEnergy.get_correct_energy_coeff(self.base_spectral_range, self.divided_spectral_range, self.spectrum_file)
                points_calibration = CorrectEnergy.get_points_calibration(self.list_captor, self.points_calibration_file, self.divided_spectral_range)
                N_mes_captor = CorrectEnergy.calibration_energy(self.N_sim_captor, integrals, points_calibration)

            CalculateEnergy.write_captor_energy(self.N_sim_captor, N_mes_captor, self.list_captor, self.divided_spectral_range, self.nb_photons)

        
        if len(self.N_sim_plant) > 0:
            CalculateEnergy.write_plant_energy(self.N_sim_plant, self.list_plant, self.divided_spectral_range, self.nb_photons)
    
    
    def visualiserSimulationScene(self, divided_spectral_range_index = -1):
        """
        Visualize the scene of simulation with the tools of OpenAlea
        To run this function, it has to run these command first:
        -- ipython
        -- %gui qt5

        Parameters
        ----------
        divided_spectral_range_index: int
            This variable allow us to visualize the color of the plant based on its received energies 

        Returns
        -------
            A rendered scene in 3D

        """

        # init visualize scene
        sc = self.scene_pgl

        #add light direction to scene
        sc = LoadEnvironment.addLightDirectionPgl(sc, self.scale_factor)

        #add plant to visualize scene
        if self.plant_file != "":
            lsystem = Lsystem(self.plant_file)
            lstring = lsystem.derive(lsystem.axiom, 150)
            plant_lscene = lsystem.sceneInterpretation(lstring)
            
            if divided_spectral_range_index == -1:
                sc = LoadPlant.addPlantModelPgl(plant_lscene, Tesselator(), sc, self.plantPos, self.scale_factor)

            elif divided_spectral_range_index >= 0 and divided_spectral_range_index < len(self.divided_spectral_range):
                #plant with energy
                sc = LoadPlant.addPlantModelPgl(plant_lscene, Tesselator(), sc, self.plantPos, self.scale_factor, self.N_sim_plant[divided_spectral_range_index])
            else:
                print("Index of range spectral is not correct.")

        #add captor
        if self.captor_file != "":
            sc = LoadCaptor.addCapteurPgl(sc, self.scale_factor, self.captor_file)
        
        Viewer.display(sc)

    def test_t_min(self, nb_photons, start_t, loop, is_only_lamp = False):
        """
        Test the simulation with multiple values of Tmin to avoid the problem of auto-intersection

        Parameters
        ----------
        nb_photons: int
            The total number of photons is shooting from the light in the simulation 
        start_t: float
            The first (smallest) value of Tmin used to run the test
        loop: int
            The number of iteration. At each iteration, the current value Tmin is multiply with 10, then run the simulation
        is_only_lamp: bool
            If True, run the test with only the lamps and captors, If False, run the test with all the objects in scene

        Returns
        -------
            A graph is generated to show the connection between the Tmin and the results of simulation

        """
                
        if loop < 1:
            return

        scene = libphotonmap_core.Scene()
        n_estimation_global = 100
        final_gathering_depth = 0 
        current_band = self.divided_spectral_range[0]
        moyenne_wavelength = (current_band["start"] + current_band["end"]) / 2
        
        list_tmin = []
        list_res = []
        list_index = []
        for i in range(loop):
            print("---------------------------------")
            print("Test Tmin =", start_t)

            scene.clear()
            scene, has_captor, captor_triangle_dict, has_plant, tr2shmap = self.initSimulationScene(scene, current_band, moyenne_wavelength, is_only_lamp)

            #create integrator
            scene.tnear = start_t
            scene.setupTriangles()
            scene.build(self.is_backface_culling)

            integrator = PhotonMapping(
                nb_photons,
                n_estimation_global,
                final_gathering_depth,
                self.max_depth,
                self.nb_thread
            )
            
            sampler = UniformSampler(1)
            
            # build no kdtree if not rendering
            integrator.build(scene, sampler, False)

            res = integrator.getPhotonMapCaptors().nPhotons()
            print("Number of photons received in total is", res)

            list_tmin.append(start_t)
            list_res.append(res)
            list_index.append(i)
            start_t = round(start_t * 10, 6)
            print("---------------------------------")

        plt.plot(list_res, linestyle='--', marker='*')
        plt.title("Number of photons received relative to the change in tmin")
        plt.ylabel("Nb of photon")
        for x, y, text in zip(list_index, list_res, list_tmin):
            plt.text(x, y, text)
        plt.show()
    

    def initSimulationScene(self, scene, current_band, moyenne_wavelength, is_only_lamp = False):
        """
        Setup all the necessary objects (environment, captor, plant) in the simulation

        Parameters
        ----------

        scene: libphotonmap_core.Scene
            The object which contains all the object in the scene of simulation
        current_band: dict
            Current divided spectral range where the simulation is running
        moyenne_wavelength: Vec3
            The average wavelength of spectral range used to determine the color of the light
        is_only_lamp: bool
            if True, only the lamps and captors is added to the scene, if False, all the objects is added. 


        Returns
        -------
            scene: libphotonmap_core.Scene
                The object which contains all the object in the scene of simulation
            has_captor: bool
                Return true if the scene has the captors 
            captor_triangle_dict: dict
                Dictionary of the triangles of the captors. Using to counting the number of photons received in each captor
            has_plant: bool
                Return true if the scene has the model of plant 
            tr2shmap: dict
                Dictionary of the triangles of the plant. Using to counting the number of photons received in each organ of plant

        """
        #add env
        materialsR, materialsS, materialsT = ReadPO.setup_dataset_materials(current_band["start"], current_band["end"], self.po_dir)
        scene.clear()
        
        for sh in self.scene_pgl:
            LoadEnvironment.add_environment(scene, sh, moyenne_wavelength, materialsR, materialsS, materialsT, is_only_lamp)

        #add plant
        has_plant = False
        tr2shmap = {}
        if(self.plant_file != ""):
            self.list_plant = LoadPlant.add_lpy_file_to_scene(scene, self.plant_file, 150, tr2shmap, self.plantPos, self.scale_factor)
            has_plant = True

        #add captor
        has_captor = False 
        captor_triangle_dict = {}
        if(self.captor_file != ""):
            self.list_captor = LoadCaptor.addCaptors(scene, self.scale_factor, captor_triangle_dict, self.captor_file)
            has_captor = True
        
        return scene, has_captor, captor_triangle_dict, has_plant, tr2shmap

    def render(self, integrator, scene, w, sampler):
        """
        Visualize the photon map of the simulation in the scene

        Parameters
        ----------
        integrator: libphotonmap_core.PhotonMapping
            The object which handles all the simulation of photon mapping
        scene: libphotonmap_core.Scene
            The object which contains all the object in the scene of simulation
        w: Vec3
            The average wavelength of spectral range used to determine the color of the light
        sampler: libphotonmap_core.Sampler
            The generator of the random number

        Returns
        -------
            Rendered images is saved into the folder ./result

        """

        if self.rendering == False:
            print("Enable rendering first !!!")
            return
        
        image = libphotonmap_core.Image(self.image_width, self.image_height)
        print("Printing photonmap image...")
        visualizePhotonMap(
            integrator,
            scene,
            image,
            self.image_height,
            self.image_width,
            self.camera,
            self.nb_photons,
            self.max_depth,
            "results/photonmap-" + str(w) + "nm.ppm",
            sampler,
        )
        image.clear()
        print("Done!")

        print("Printing captor photonmap image...")
        visualizeCaptorsPhotonMap(
            scene,
            image,
            self.image_height,
            self.image_width,
            self.camera,
            self.nb_photons,
            self.max_depth,
            "results/photonmap-captors-" + str(w) + "nm.ppm",
            sampler,
            integrator,
        )
        image.clear()
        print("Done!")
            

    def setupRoom(self, room_file: str, po_dir: str,  flip_normal = False):
        """
        Setup the room/environment of the simulation.

        Parameters
        ----------
        room_file: str
            The link to the file which contains the geometries of the room
        po_dir: str
            The link to the folder which contains the optical properties of the room
        flip_normal: bool
            Determine the direction of the vector normal of triangle. 
        """
        self.po_dir = po_dir
        self.scene_pgl = ReadRADGeo.read_rad(room_file, self.scale_factor, flip_normal)

    def setupRender(self, lookfrom = Vec3(0,0,0), lookat = Vec3(0,0,0)):
        """
        Enable the capacity to render/visulize the photon map in the scene

        Parameters
        ----------
        lookfrom: Vec3
            The position of the camera.
        lookat: Vec3
            The point where the camera is looking at
                
        """
        self.rendering = True
        #using for render the results
        self.camera = self.initCameraRender(lookfrom, lookat)

    def setupCaptor(self, captor_file: str, spectrum_file: str, points_calibration_file: str):
        """
        Setup the captors in the simulation. Enable the capacity to run the simulation with the circle captors 

        Parameters
        ----------
        captor_file: str
            The link to the file which contains the informations of the captors in the simulation
        spectrum_file: str
            The link to the file which contains the informations of the heterogeneity of the spectrum
        points_calibration_file: str
            The link to the file which contains the informations of the captors used to calibrate the final result 
                
        """
        self.captor_file = captor_file
        self.spectrum_file = spectrum_file
        self.points_calibration_file = points_calibration_file

    def setupPlant(self, plant_file: str, plant_pos = Vec3(0,0,0)):
        """
        Setup a plant in the simulation. Enable the capacity to run the simulation with a model of plant

        Parameters
        ----------
        plant_file: str
            The link to the file of the model of plant. (currently only support .lpy file)
        plantPos: Vec3
            The position of the plant
                
        """
        self.plant_file = plant_file
        self.plantPos = plant_pos
        

    def initCameraRender(self, lookfrom = Vec3(0,0,0), lookat = Vec3(0,0,0)):
        """
        Init the camera to render image. Calling by the function setupRender

        Parameters
        ----------
        lookfrom: Vec3
            The position of the camera.
        lookat: Vec3
            The point where the camera is looking at
                
        Returns
        -------
        camera: libphotonmap_core.Camera
            An object with all the informations of camera
        """

        aspect_ratio = 16.0 / 9.0
        self.image_width = 512
        self.image_height = 512

        vup = Vec3(0, 0, -1)
        vfov = 50.0
        dist_to_focus = 2.0
        aperture = 0.01

        # coordinates must be in meters
        camera = libphotonmap_core.Camera(
            lookfrom, lookat, vup, vfov, aspect_ratio, aperture, dist_to_focus
        )

        return camera

    def readConfiguration(self, filename: str):
        """
        Read all the parameters of simulation in the configuration file

        Parameters
        ----------
        filename: str
            Name/directory of the configuration file.
            
        """
        #read file
        with open(filename, "r") as f:
            next(f)
            for line in f:
                if "$" in line:
                    row = line.replace("\n", "").split(" ")
    
                    match row[0]:
                        case "$NB_PHOTONS":
                            self.nb_photons = int(row[1])
                        case "$MAXIMUM_DEPTH":
                            self.max_depth = int(row[1])
                        case "$SCALE_FACTOR":
                            self.scale_factor = int(row[1])
                        case "$T_MIN":
                            self.t_min = float(row[1])
                        case "$NB_THREAD":
                            self.nb_thread = int(row[1])
                        case "$BACKFACE_CULLING":
                            self.is_backface_culling = True if (row[1].upper() == "YES") else False 
                        case "$BASE_SPECTRAL_RANGE":
                            self.base_spectral_range = {"start": int(row[1]), "end": int(row[2])}
                        case "$DIVIDED_SPECTRAL_RANGE":
                            nb_bande = int(row[1])
    
                            for i in range(nb_bande):
                                start = int(row[(i + 1) * 2])
                                end = int(row[(i + 1) * 2 + 1])
                                self.divided_spectral_range.append({"start": start, "end": end})
        
    

