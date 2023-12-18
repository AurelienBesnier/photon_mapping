from photonmap import Camera, Image, Ray, Vec2, Vec3, Scene, IntersectInfo, Render, UniformSampler, PhotonMapping
import random, sys, os


def test_intersection():
    scene = Scene()
    scene.loadModel("./tests/cornellbox-water2.obj")
    scene.build()
    
    n_samples = 1
    n_photons = int(1e3)
    n_estimation_global = 100
    n_photons_caustics_multiplier = 50
    n_estimation_caustics = 50
    final_gathering_depth = 0
    max_depth = 24

    aspect_ratio = 16.0 / 9.0

    image_width = 1024
    image_height = int(image_width / aspect_ratio)

    lookfrom = Vec3(0, 1, 7)
    lookat = Vec3(0, 0, -1)
    vup = Vec3(0, 1, 0)
    vfov = 50.0
    dist_to_focus = 3.0
    aperture = 0.01

    camera = Camera(lookfrom, lookat, vup, vfov, aspect_ratio,
                    aperture, dist_to_focus)

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
    
