import sys
import random

from photonmap.libphotonmap_core import *

from datetime import datetime

if __name__ == '__main__':
    width = 512
    height = 512
    n_samples = 25
    n_photons = 10000
    n_estimation_global = 95
    n_photons_caustics_multiplier = 50
    n_estimation_caustics = 50
    final_gathering_depth = 4
    max_depth = 100

    image = Image(width, height)
    camera = Camera(Vec3(0, 5, -7), Vec3(0.4, -0.4, 1), 0.5 * PI)

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

    print("Creating Scene..")
    scene = Scene()
    scene.loadModel("mesh.obj")
    scene.build()

    print("Done!")

    print("Building photonMap...")
    integrator = PhotonMapping(n_photons, n_estimation_global,
                               n_photons_caustics_multiplier, n_estimation_caustics,
                               final_gathering_depth, max_depth)

    sampler = UniformSampler(random.randint(0, sys.maxsize))

    integrator.build(scene, sampler)
    print("Done!")

    print("Printing photonmap image...")
    visualizePhotonMap(scene, image, width, height, camera, n_photons, max_depth, "photonmap.ppm")
    print("Done!")

    print("Rendering image...")
    image = Image(width, height)
    Render(sampler, image, height, width, n_samples, camera, integrator, scene, "output-photonmapping.ppm")

    print("Done!")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

    print("You did it !")
