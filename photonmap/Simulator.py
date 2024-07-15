import random
import sys
import time

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


class Simulator:
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
        self.plant_dir = ""
        self.po_dir = ""
        

    def run(self):
        scene = libphotonmap_core.Scene()
        n_estimation_global = 100
        final_gathering_depth = 0 

        for index in range(len(self.bande_spectre)):
            
            start_time = time.time()
            current_band = self.bande_spectre[index]
            moyenne_wavelength = (current_band["start"] + current_band["end"]) / 2
            #add env
            materialsR, materialsS, materialsT = ReadPO.setup_dataset_materials(current_band["start"], current_band["end"], self.po_dir)
            scene.clear()
            
            for sh in self.scene_pgl:
                LoadEnvironment.add_environment(scene, sh, moyenne_wavelength, materialsR, materialsS, materialsT)

            #add plant
            has_plant = False
            tr2shmap = {}
            if(self.plant_dir != ""):
                LoadPlant.add_lpy_file_to_scene(scene, self.plant_dir, 128, tr2shmap, self.anchor, self.scale_factor)
                has_plant = True

            #add captor
            has_captor = False 
            captor_dict = {}
            if(self.captor_dir != ""):
                LoadCaptor.addCaptors(scene, self.scale_factor, captor_dict, self.captor_dir)
                has_captor = True
            
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
            integrator.build(scene, sampler, False)
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

            # Setting up spectrum bands to correct energy
            #spec_file = "spectrum/chambre1_spectrum"
            #self.wavelengths, self.integrals = CorrectEnergy.get_correct_energy_coeff(self.bande_spectre, spec_file)
            # print("correction ratio: " + str(integrals[index]))
            # correct_energy(captor_energy, integrals[index])

            #sc = addPlantModelPgl(lscene, Tesselator(), sc, anchor, scale_factor, captor_energy)
            #sc = addCapteurPgl(sc, scale_factor, "captors/captors_expe1.csv")
            #sc = addLightDirectionPgl(sc, scale_factor)
            #Viewer.display(sc)      
            

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
            
        print("Rendering image...")
        image = libphotonmap_core.Image(self.image_width, self.image_height)
        Render(
            sampler,
            image,
            self.image_height,
            self.image_width,
            self.camera,
            self.nb_photons,
            integrator,
            scene,
            "results/output-photonmapping-" + str(w) + "nm.ppm",
        )

        image.clear()

    def setupRoom(self, room_dir: str, po_dir: str,  flip_normal = False):
        self.po_dir = po_dir
        self.scene_pgl, self.anchor, self.scale_factor = ReadRADGeo.read_rad(room_dir, flip_normal)

    def setupRender(self):
        self.rendering = True
        #using for render the results
        self.camera = self.initCameraRender(self.anchor)

    def setupCaptor(self, captor_dir: str):
        self.captor_dir = captor_dir

    def setupPlant(self, plant_dir: str):
        self.plant_dir = plant_dir
        

    def initCameraRender(self, anchor):
        aspect_ratio = 16.0 / 9.0
        self.image_width = 1024
        self.image_height = int(self.image_width / aspect_ratio)

        lookfrom = Vec3(1.5, 1.5, 1.5)
        lookat = Vec3(anchor[0], anchor[1], anchor[2])
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
                        case "$CAPTOR_DIR":
                            self.captor_dir = row[1]
                        case "$BANDES_SPECTRE":
                            nb_bande = int(row[1])
    
                            for i in range(nb_bande):
                                start = int(row[(i + 1) * 2])
                                end = int(row[(i + 1) * 2 + 1])
                                self.bande_spectre.append({"start": start, "end": end})
        
    

