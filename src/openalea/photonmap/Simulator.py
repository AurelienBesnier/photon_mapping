import os
import random
import sys
import time

import matplotlib.pyplot as plt

from openalea.lpy import Lsystem
from openalea.photonmap import (
    PhotonMapping,
    UniformSampler,
    Vec3,
    libphotonmap_core,
)
from openalea.photonmap.Energy import CalculateEnergy, CorrectEnergy
from openalea.photonmap.libphotonmap_core import (
    Render,
    visualizeCaptorsPhotonMap,
    visualizePhotonMap,
)
from openalea.photonmap.Loader import LoadCaptor, LoadEnvironment
from openalea.photonmap.Reader import ReadPO, ReadRADGeo
from openalea.plantgl.all import *


class SimulationResult:
    """
    A class which contains the result of simulation.

    Attributes
    ----------

    N_sim_virtual_captor: dict
        Number of received photons on each captor
    N_sim_face_captor: dict
        Number of received photons on each organ of plant
    N_mes_virtual_captor: dict
        The energies after the calibration on each captor
    N_mes_face_captor: dict
        The energies after the calibration on each organ of plant

    nb_photons: int
        The number of photons in simulation
    divided_spectral_range: array
        The list of spectral ranges divided from the base spectral range.

    list_virtual_captor: array
        The list of virtual captor in simulation

    """

    # constructor

    def __init__(self, simulator):
        self.photonmaps = simulator.photonmaps

        self.N_sim_virtual_captor = simulator.N_sim_virtual_captor
        self.N_sim_face_captor = simulator.N_sim_face_captor
        self.N_mes_virtual_captor = simulator.N_mes_virtual_captor
        self.N_mes_face_captor = simulator.N_mes_face_captor

        self.divided_spectral_range = simulator.divided_spectral_range
        self.list_virtual_captor = simulator.list_virtual_captor
        self.list_face_captor = simulator.list_face_captor

    def writeResults(self, file_prefix=""):
        """
        Write the result of simulation to a file saved in the folder ./results

        Parameters
        ----------
        file_prefix: str
            The prefix of output file
        """

        if len(self.N_sim_virtual_captor) > 0:
            CalculateEnergy.write_captor_energy(
                self.N_sim_virtual_captor,
                self.N_mes_virtual_captor,
                self.list_virtual_captor,
                self.divided_spectral_range,
                file_prefix + "virtual_captor_res.csv",
            )

        if len(self.N_sim_face_captor) > 0:
            CalculateEnergy.write_captor_energy(
                self.N_sim_face_captor,
                self.N_mes_face_captor,
                self.list_face_captor,
                self.divided_spectral_range,
                file_prefix + "face_captor_res.csv",
            )

    def graph(self):
        """
        Draw a graph with MathPlotlib

        """
        return


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
    N_sim_virtual_captor: dict
        Number of received photons on each captor
    N_sim_face_captor: dict
        Number of received photons on each organ of plant

    spectrum_file: str
        The link to the file which contains the informations of the heterogeneity of the spectrum
    points_calibration_file: str
        The link to the file which contains the informations of the captors used to calibrate the final result

    list_virtual_captor: array
        The list of virtual captor in simulation
    pgl_scene: openalea.plantgl.scenegraph.Scene
        The plantgl scene object used to save the meshs of environment
    plantPos: Vec3
        The position of the plant
    po_dir: str
        The link to the folder which contains the optical properties of the room

    """

    # constructor

    def __init__(self):
        self.nb_photons = 0
        self.n_samples = 512
        self.max_depth = 0
        self.scale_factor = 1
        self.t_min = 0.0001
        self.nb_thread = 8
        self.is_backface_culling = False
        self.base_spectral_range = {"start": 0, "end": 0}
        self.divided_spectral_range = [{"start": 0, "end": 0}]
        self.rendering = False
        #
        self.scene_pgl = Scene()
        self.list_virtual_captor = []
        self.list_face_captor = []

        # result
        self.N_sim_virtual_captor = []
        self.N_sim_face_captor = []
        self.N_mes_virtual_captor = []
        self.N_mes_face_captor = []
        self.photonmaps = []

        self.image_width = 512
        self.image_height = 512

        # input files
        self.po_dir = ""
        self.spectrum_file = ""
        self.points_calibration_file = ""

    def resetScene(self):
        """
        Clear list of captors and list of object in scene
        """
        self.scene_pgl.clear()
        self.list_virtual_captor.clear()
        self.list_face_captor.clear()

    def addEnvToScene(self, sh):
        """
        Add a environment's object to scene

        Parameters
        ----------
        sh : plantgl.Shape
            The mesh of object

        Returns
        -------
            The object is added to the scene

        """
        vertices = sh.geometry.pointList
        # apply scale factor
        for i in range(len(vertices)):
            vertices[i] = tuple(x / self.scale_factor for x in vertices[i])

        sh.geometry.pointList = vertices
        sh.geometry.computeNormalList()

        # add object to scene
        self.scene_pgl.add(sh)

    def addFaceCaptorToScene(self, shape, position, scale_factor):
        """
        Add a face captor object to scene

        Parameters
        ----------
        shape: Shape
            The geometry and material of captor
        position : tuple(int,int,int)
            The position of captor
        scale_factor: int
            The size of geometries. The vertices of geometries is recalculated by dividing their coordinates by this value

        Returns
        -------
            The face captor is added to the scene

        """
        captor = LoadCaptor.Captor().initCaptor(
            shape, position, scale_factor, "FaceCaptor"
        )
        self.list_face_captor.append(captor)

    def addVirtualCaptorToScene(self, shape, position, scale_factor):
        """
        Add a virtual captor object to scene

        Parameters
        ----------
        shape: Shape
            The geometry and material of captor
        position : tuple(int,int,int)
            The position of captor
        scale_factor: int
            The size of geometries. The vertices of geometries is recalculated by dividing their coordinates by this value

        Returns
        -------
            The virtual captor is added to the scene

        """
        captor = LoadCaptor.Captor().initCaptor(
            shape, position, scale_factor, "VirtualCaptor"
        )
        self.list_virtual_captor.append(captor)

    def addVirtualDiskCaptorToScene(self, pos, normal, r, captor_id):
        """
        Add a virtual disk shaped captor object to scene

        Parameters
        ----------
        pos : tuple(float,float,float)
            The position of captor
        normal: tuple(float,float,float)
            The vector normal of captor
        r: float
            The radius of captor
        captor_id: int
            The id of captor

        Returns
        -------
            The disk shaped captor is added to the scene

        """
        captor = LoadCaptor.Captor().initVirtualDiskCaptor(
            (
                pos[0] / self.scale_factor,
                pos[1] / self.scale_factor,
                pos[2] / self.scale_factor,
            ),
            (normal[0], normal[1], normal[2]),
            r,
            captor_id,
        )

        self.list_virtual_captor.append(captor)

    def run(self):
        """
        Run the simulation with the configurations which is determined

        Returns
        -------
            The number of received photons on each captor and organs of plant is saved into the files located in folde ./results

        """

        self.photonmaps.clear()
        self.N_sim_face_captor.clear()
        self.N_sim_virtual_captor.clear()
        self.N_mes_virtual_captor.clear()
        self.N_mes_face_captor.clear()

        scene = libphotonmap_core.Scene()
        n_estimation_global = 100
        final_gathering_depth = 0

        for index in range(len(self.divided_spectral_range)):
            start_time = time.time()
            current_band = self.divided_spectral_range[index]

            print("Wavelength:", current_band["start"], "-", current_band["end"])
            moyenne_wavelength = (current_band["start"] + current_band["end"]) / 2
            scene.clear()
            (
                scene,
                has_virtual_captor,
                virtual_captor_triangle_dict,
                has_face_captor,
                face_captor_triangle_dict,
            ) = self.initSimulationScene(scene, current_band, moyenne_wavelength)

            # create integrator
            scene.tnear = self.t_min
            scene.setupTriangles()
            scene.build(self.is_backface_culling)

            integrator = PhotonMapping(
                self.nb_photons,
                n_estimation_global,
                final_gathering_depth,
                self.max_depth,
                self.nb_thread,
            )

            print("Build photonMap...")

            sampler = UniformSampler(random.randint(1, sys.maxsize))

            # build no kdtree if not rendering
            integrator.build(scene, sampler, self.rendering)
            print("Done!")

            # rendering if declared
            if self.rendering:
                self.render(integrator, scene, moyenne_wavelength, sampler)

            # read energy of virtual captor
            virtual_captor_energy = {}
            if has_virtual_captor:
                CalculateEnergy.captor_add_energy(
                    virtual_captor_triangle_dict, integrator, virtual_captor_energy
                )
                self.N_sim_virtual_captor.append(virtual_captor_energy)

            # read energy of face captor
            face_captor_energy = {}
            if has_face_captor:
                CalculateEnergy.captor_add_energy(
                    face_captor_triangle_dict, integrator, face_captor_energy
                )
                self.N_sim_face_captor.append(face_captor_energy)

            self.photonmaps.append(integrator.getPhotonMapCaptors())
            print("Time taken: " + str(time.time() - start_time))

        return SimulationResult(self)

    def calculateCalibrationCoefficient(
        self, spectrum_file="", points_calibration_file=""
    ):
        """
        Calculate the coefficients which is used to calibrate the final result of simulation with the captors

        Parameters
        ----------
        spectrum_file: str
            The link to the file which contains the informations of the heterogeneity of the spectrum
        points_calibration_file: str
            The link to the file which contains the informations of the captors used to calibrate the final result

        """

        self.coeffs_calibration = []

        if os.path.exists(spectrum_file) and os.path.exists(points_calibration_file):
            self.integrals = CorrectEnergy.get_correct_energy_coeff(
                self.base_spectral_range, self.divided_spectral_range, spectrum_file
            )
            self.points_calibration = CorrectEnergy.get_points_calibration(
                self.list_virtual_captor,
                points_calibration_file,
                self.divided_spectral_range,
            )
            self.coeffs_calibration = CorrectEnergy.get_calibaration_coefficient(
                self.N_sim_virtual_captor, self.integrals, self.points_calibration
            )
            return True

        return False

    def calibrateResults(self, spectrum_file="", points_calibration_file=""):
        """
        Calibrate the final result of simulation

        Parameters
        ----------
        spectrum_file: str
            The link to the file which contains the informations of the heterogeneity of the spectrum
        points_calibration_file: str
            The link to the file which contains the informations of the captors used to calibrate the final result

        """

        can_calibrate = self.calculateCalibrationCoefficient(
            spectrum_file, points_calibration_file
        )

        if can_calibrate:
            if len(self.N_sim_virtual_captor) > 0:
                self.N_mes_virtual_captor = CorrectEnergy.calibrate_captor_energy(
                    self.N_sim_virtual_captor,
                    self.integrals,
                    self.points_calibration,
                    self.coeffs_calibration,
                )

            if len(self.coeffs_calibration) > 0 and len(self.N_sim_face_captor) > 0:
                self.N_mes_face_captor = CorrectEnergy.calibrate_plant_energy(
                    self.N_sim_face_captor, self.coeffs_calibration
                )

        return SimulationResult(self)

    def visualiserSimulationScene(self, mode="ipython"):
        """
        Visualize the scene of simulation with the tools of OpenAlea
        To run this function, it has to run these command first:
        -- ipython
        -- %gui qt5

        Parameters
        ----------
        mode: str
            This variable define the mode used to visualize the scene. There are the supported modes: ipython, pgljupyter

        Returns
        ---z----
            A rendered scene in 3D

        """

        # init visualize scene
        sc = self.scene_pgl

        # add light direction to scene
        # sc = LoadEnvironment.addLightDirectionPgl(sc, self.scale_factor)

        # add face captor
        if len(self.list_face_captor) > 0:
            sc = LoadCaptor.addCaptorPgl(sc, self.list_face_captor)

        # add captor
        if len(self.list_virtual_captor) > 0:
            sc = LoadCaptor.addCaptorPgl(sc, self.list_virtual_captor)

        if mode == "ipython":
            Viewer.display(sc)

        elif mode == "oawidgets":
            from oawidgets.plantgl import PlantGL

            return PlantGL(sc)

        else:
            Viewer.display(sc)

    def test_t_min(self, nb_photons, start_t, loop, is_only_lamp=False):
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

        scene.clear()
        (
            scene,
            has_virtual_captor,
            virtual_captor_triangle_dict,
            has_face_captor,
            face_captor_triangle_dict,
        ) = self.initSimulationScene(
            scene, current_band, moyenne_wavelength, is_only_lamp
        )
        # create integrator
        scene.setupTriangles()
        scene.build(self.is_backface_culling)

        for i in range(loop):
            print("---------------------------------")
            print("Test Tmin =", start_t)
            scene.tnear = start_t

            integrator = PhotonMapping(
                nb_photons,
                n_estimation_global,
                final_gathering_depth,
                self.max_depth,
                self.nb_thread,
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

        plt.plot(list_index, list_res, linestyle="--", marker="*")
        plt.title("Number of photons received relative to the change in tmin")
        plt.ylabel("Nb of photon")
        for x, y, text in zip(list_index, list_res, list_tmin):
            plt.text(x, y, text)
        plt.show()

    def initSimulationScene(
        self, scene, current_band, moyenne_wavelength, is_only_lamp=False
    ):
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
            has_virtual_captor: bool
                Return true if the scene has the captors
            captor_triangle_dict: dict
                Dictionary of the triangles of the captors. Using to counting the number of photons received in each captor
            has_plant: bool
                Return true if the scene has the model of plant
            tr2shmap: dict
                Dictionary of the triangles of the plant. Using to counting the number of photons received in each organ of plant

        """
        # add env
        materials_r, materials_s, materials_t = ReadPO.setup_dataset_materials(
            current_band["start"], current_band["end"], self.po_dir
        )
        scene.clear()

        for sh in self.scene_pgl:
            LoadEnvironment.addEnvironment(
                scene,
                sh,
                moyenne_wavelength,
                materials_r,
                materials_s,
                materials_t,
                is_only_lamp,
            )

        # add face captor
        has_face_captor = False
        face_captor_triangle_dict = {}

        if len(self.list_face_captor) > 0:
            LoadCaptor.addFaceCaptors(
                scene, face_captor_triangle_dict, self.list_face_captor
            )
            has_face_captor = True

        # add virtual captor
        has_virtual_captor = False
        virtual_captor_triangle_dict = {}

        if len(self.list_virtual_captor) > 0:
            LoadCaptor.addVirtualCaptors(
                scene, virtual_captor_triangle_dict, self.list_virtual_captor
            )
            has_virtual_captor = True

        return (
            scene,
            has_virtual_captor,
            virtual_captor_triangle_dict,
            has_face_captor,
            face_captor_triangle_dict,
        )

    def render(self, integrator, scene, w, sampler):
        """
        Visualize the photon map of the scene and render an image from it.

        Parameters
        ----------
        integrator: libphotonmap_core.PhotonMapping
            The object which handles all the simulation of photon mapping.
        scene: libphotonmap_core.Scene
            The object which contains all the object in the scene of simulation.
        w: Vec3
            The average wavelength of spectral range used to determine the color of the light.
        sampler: libphotonmap_core.Sampler
            The generator of the random number.

        Returns
        -------
            Rendered images is saved into the folder ./result

        """

        if not os.path.exists("results"):
            os.makedirs("results")

        if not self.rendering:
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
        Render(
            sampler,
            image,
            self.image_height,
            self.image_width,
            self.n_samples,
            self.camera,
            integrator,
            scene,
            "results/render-" + str(w) + "nm.ppm",
        )
        image.clear()
        print("Done!")

    def addEnvFromFile(self, room_file: str, po_dir: str, flip_normal=False):
        """
        Setup the room/environment of the simulation from file.

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

    def setupRender(self, lookfrom=Vec3(0, 0, 0), lookat=Vec3(0, 0, 0), vfov=50.0):
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
        # using for render the results
        self.camera = self.initCameraRender(lookfrom, lookat, vfov)

    def addVirtualDiskCaptorsFromFile(self, captor_file: str):
        """
        Setup the captors in the simulation. Enable the capacity to run the simulation with the circle captors

        Parameters
        ----------
        captor_file: str
            The link to the file which contains the informations of the captors in the simulation

        """

        if captor_file != "":
            captor_id = len(self.list_virtual_captor)
            with open(captor_file, encoding="UTF8") as f:
                next(f)
                for line in f:
                    row = line.split(",")
                    x = float(row[0])
                    y = float(row[1])
                    z = float(row[2])
                    r = float(row[3])
                    xnorm = float(row[4])
                    ynorm = float(row[5])
                    znorm = float(row[6])

                    self.addVirtualDiskCaptorToScene(
                        (x, y, z), (xnorm, ynorm, znorm), r, captor_id
                    )
                    captor_id += 1

    def addFaceCaptorsFromLpyFile(
        self, plant_file: str, plant_pos=Vec3(0, 0, 0), derivation_length=None
    ):
        """
        Setup a plant in the simulation. Enable the capacity to run the simulation with a model of plant

        Parameters
        ----------
        plant_file: str
            The link to the file of the model of plant. (currently only support .lpy file)
        plantPos: Vec3
            The position of the plant
        derivation_length: int
            The number of iteration to interpret the plant
        """

        lsystem = Lsystem(plant_file)
        if derivation_length is None:
            derivation_length = lsystem.derivationLength

        lstring = lsystem.derive(lsystem.axiom, derivation_length)
        lscene = lsystem.sceneInterpretation(lstring)

        scale_factor = self.scale_factor / 10
        position = (plant_pos[0] / 10, plant_pos[1] / 10, plant_pos[2] / 10)

        tr = Tesselator()
        for sh in lscene:
            sh.apply(tr)
            mesh = Shape(tr.result, sh.appearance, sh.id)
            self.addFaceCaptorToScene(mesh, position, scale_factor)

    def initCameraRender(self, lookfrom=Vec3(0, 0, 0), lookat=Vec3(0, 0, 0), vfov=50.0):
        """
        Init the camera to render image. Called by the function setupRender

        Parameters
        ----------
        lookfrom: Vec3
            The position of the camera.
        lookat: Vec3
            The point where the camera is looking at

        Returns
        -------
        camera: libphotonmap_core.Camera
            An object with all the information of camera
        """

        aspect_ratio = 16.0 / 9.0

        vup = Vec3(0, 0, -1)
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
        # read file
        with open(filename, encoding="UTF8") as f:
            next(f)
            for line in f:
                if "$" in line:
                    row = line.replace("\n", "").split(" ")

                    if row[0] == "$NB_PHOTONS":
                        self.nb_photons = int(row[1])
                    elif row[0] == "$MAXIMUM_DEPTH":
                        self.max_depth = int(row[1])
                    elif row[0] == "$SCALE_FACTOR":
                        self.scale_factor = int(row[1])
                    elif row[0] == "$T_MIN":
                        self.t_min = float(row[1])
                    elif row[0] == "$NB_THREAD":
                        self.nb_thread = int(row[1])
                    elif row[0] == "$BACKFACE_CULLING":
                        self.is_backface_culling = (
                            True if (row[1].upper() == "YES") else False
                        )
                    elif row[0] == "$BASE_SPECTRAL_RANGE":
                        self.base_spectral_range = {
                            "start": int(row[1]),
                            "end": int(row[2]),
                        }
                    elif row[0] == "$DIVIDED_SPECTRAL_RANGE":
                        nb_bande = int(row[1])
                        self.divided_spectral_range.clear()

                        for i in range(nb_bande):
                            start = int(row[(i + 1) * 2])
                            end = int(row[(i + 1) * 2 + 1])
                            self.divided_spectral_range.append(
                                {"start": start, "end": end}
                            )
