import os
import random
import sys

from openalea.spice import (
    Camera,
    Image,
    PhotonMapping,
    Render,
    Scene,
    UniformSampler,
    Vec3,
)


def test_intersection():
    scene = Scene()
    scene.loadModel("./tests/cornellbox-water2.obj")
    scene.build(True)

    n_samples = 2
    n_photons = 10000
    n_estimation_global = 100
    n_photons_caustics_multiplier = 50
    n_estimation_caustics = 50
    final_gathering_depth = 1
    max_depth = 5

    aspect_ratio = 1

    image_width = 600
    image_height = int(image_width / aspect_ratio)

    lookfrom = Vec3(-0.4, 1, 3)
    lookat = Vec3(-1, -0.19, -2.5)
    vup = Vec3(0, -1, 0)
    vfov = 30.0
    dist_to_focus = 3.0
    aperture = 0.01

    camera = Camera(lookfrom, lookat, vup, vfov, aspect_ratio, aperture, dist_to_focus)

    image = Image(image_width, image_height)

    sampler = UniformSampler(random.randint(1, sys.maxsize))
    integrator = PhotonMapping(
        n_photons,
        n_estimation_global,
        n_photons_caustics_multiplier,
        n_estimation_caustics,
        final_gathering_depth,
        max_depth,
    )

    integrator.build(scene, sampler, True)
    Render(
        sampler,
        image,
        image_height,
        image_width,
        n_samples,
        camera,
        integrator,
        scene,
        "output.ppm",
    )

    image.writePPM("output.ppm")
    intersection_worked = True
    assert intersection_worked
    os.remove("output.ppm")
