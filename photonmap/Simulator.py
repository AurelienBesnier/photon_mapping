import random
import sys
import time

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
    name : str
        first name of the person
    surname : str
        family name of the person
    age : int
        age of the person

    Methods
    -------
    info(additional=""):
        Prints the person's name and age.
    """
    #constructor
    def __init__(self):
        self.nb_photons = 0
        self.max_depth = 0
        self.scale_factor = 1
        self.t_min = 0
        self.nb_thread = 8
        self.is_backface_culling = False
        self.bande_spectre = []
        self.rendering = False
        #
        self.captor_dir = ""
        self.plant_file = ""
        self.po_dir = ""
        

    def run(self):
        scene = libphotonmap_core.Scene()
        n_estimation_global = 100
        final_gathering_depth = 0 

        # Setting up spectrum bands to correct energy
        spec_file = "spectrum/chambre1_spectrum"
        self.wavelengths, self.integrals = CorrectEnergy.get_correct_energy_coeff(self.bande_spectre, spec_file)

        for index in range(len(self.bande_spectre)):
            start_time = time.time()
            current_band = self.bande_spectre[index]
            
            print("Wavelength:", current_band["start"], "-", current_band["end"])
            moyenne_wavelength = (current_band["start"] + current_band["end"]) / 2
            scene.clear()
            scene, has_captor, captor_dict, has_plant, tr2shmap = self.initSimulationScene(scene, current_band, moyenne_wavelength)
            
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
                CalculateEnergy.captor_add_energy(captor_dict, integrator, captor_energy)
                CalculateEnergy.write_captor_energy(captor_energy, current_band["start"], current_band["end"], self.nb_photons)

            #Plant Energie
            plant_energy = {}
            if(has_plant):
                plant_energy = CalculateEnergy.compute_energy(tr2shmap, integrator)
                CalculateEnergy.write_plant_energy(plant_energy, current_band["start"], current_band["end"], self.nb_photons)
            
            print("Time taken: " + str(time.time() - start_time))

            
            print("correction ratio: " + str(self.integrals[index]))

            # correct_energy(captor_energy, integrals[index])

            #sc = addPlantModelPgl(lscene, Tesselator(), sc, anchor, scale_factor, captor_energy)
            #sc = addCapteurPgl(sc, scale_factor, "captors/captors_expe1.csv")
            #sc = addLightDirectionPgl(sc, scale_factor)
            #Viewer.display(sc)      
            
    def test_t_min(self, nb_photons, start_t, loop, is_only_lamp = False):
        if loop < 1:
            return

        scene = libphotonmap_core.Scene()
        n_estimation_global = 100
        final_gathering_depth = 0 
        current_band = self.bande_spectre[0]
        moyenne_wavelength = (current_band["start"] + current_band["end"]) / 2
        
        list_tmin = []
        list_res = []
        list_index = []
        for i in range(loop):
            print("---------------------------------")
            print("Test Tmin =", start_t)

            scene.clear()
            scene, has_captor, captor_dict, has_plant, tr2shmap = self.initSimulationScene(scene, current_band, moyenne_wavelength, is_only_lamp)

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
        
        #add env
        materialsR, materialsS, materialsT = ReadPO.setup_dataset_materials(current_band["start"], current_band["end"], self.po_dir)
        scene.clear()
        
        for sh in self.scene_pgl:
            LoadEnvironment.add_environment(scene, sh, moyenne_wavelength, materialsR, materialsS, materialsT, is_only_lamp)

        #add plant
        has_plant = False
        tr2shmap = {}
        if(self.plant_file != ""):
            LoadPlant.add_lpy_file_to_scene(scene, self.plant_file, 128, tr2shmap, self.plantPos, self.scale_factor)
            has_plant = True

        #add captor
        has_captor = False 
        captor_dict = {}
        if(self.captor_dir != ""):
            LoadCaptor.addCaptors(scene, self.scale_factor, captor_dict, self.captor_dir)
            has_captor = True
        
        return scene, has_captor, captor_dict, has_plant, tr2shmap

    def render(self, integrator, scene, w, sampler):
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
            

    def setupRoom(self, room_dir: str, po_dir: str,  flip_normal = False):
        self.po_dir = po_dir
        self.scene_pgl = ReadRADGeo.read_rad(room_dir, self.scale_factor, flip_normal)

    def setupRender(self, lookfrom = Vec3(0,0,0), lookat = Vec3(0,0,0)):
        self.rendering = True
        #using for render the results
        self.camera = self.initCameraRender(lookfrom, lookat)

    def setupCaptor(self, captor_dir: str):
        self.captor_dir = captor_dir

    def setupPlant(self, plant_file: str, plant_pos = Vec3(0,0,0)):
        self.plant_file = plant_file
        self.plantPos = plant_pos
        

    def initCameraRender(self, lookfrom = Vec3(0,0,0), lookat = Vec3(0,0,0)):
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
            
        Returns
        -------
        nb_photons: int
            The number of photons in simulation
        maximum_depth: int
            The maximum number of times that the light bounces in the scene 
        scale_factor: float
            The overall scale of the entire scene
        t_min: float
            The minimum distance between the point of intersection and the origin of the light ray
        nb_thread: int
            The number of threads on the CPU used to calculate in parallel. This value is between 0 and the number of cores of your CPU.
        is_backface_culling: bool
            Define which mode of intersection is chosen: intersect only with the front face or intersect with both faces.
        bande_spectre: array
            The list of spectral ranges used to run the simulation.
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
                        case "$BANDES_SPECTRE":
                            nb_bande = int(row[1])
    
                            for i in range(nb_bande):
                                start = int(row[(i + 1) * 2])
                                end = int(row[(i + 1) * 2 + 1])
                                self.bande_spectre.append({"start": start, "end": end})
        
    

