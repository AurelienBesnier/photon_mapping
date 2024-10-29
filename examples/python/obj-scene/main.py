from datetime import datetime
import random
import sys

from photonmap.libphotonmap_core import *

if __name__ == '__main__':
    n_samples = 2
    n_photons = 100
    n_estimation_global = 95
    n_photons_caustics_multiplier = 20
    n_estimation_caustics = 10
    final_gathering_depth = 2
    max_depth = 2
    
    aspect_ratio = 4/3
    image_width = 512
    image_height = int(image_width / aspect_ratio)
    image = Image(image_width, image_height)

    lookfrom = Vec3(6.1, 2.4, -7)
    lookat = Vec3(6.6, 2.0, 1.0)
    vup = Vec3(0, -1, 0)
    vfov = 20.0
    dist_to_focus = 5.0
    aperture = 0.01

    # coordinates must be in meters
    camera = Camera(
        lookfrom, lookat, vup, vfov, aspect_ratio, aperture, dist_to_focus
    )

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

    integrator.build(scene, sampler, True)
    print("Done!")

    print("Printing photonmap image...")
    visualizePhotonMap(
                integrator,
                scene,
                image,
                image_height,
                image_width,
                camera,
                n_photons,
                max_depth,
                "photonmap.ppm",
                sampler,
            )
    print("Done!")

    print("Rendering image...")
    image = Image(image_width, image_height)
    Render(
            sampler,
            image,
            image_height,
            image_width,
            n_samples,
            camera,
            integrator,
            scene,
            "output-photonmapping.ppm",
        )

    print("Done!")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

    print("You did it !")
