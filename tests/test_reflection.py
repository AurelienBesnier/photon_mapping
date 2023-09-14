from photonmap.libphotonmap_core import *
import random
import sys

def test_reflection():
    """Test if photon from a light source all end up on an absorbing surface."""
    scene = Scene()
    scene.loadModel("testChamberPH.obj")
    pos = Vec3(0.5, 0.5, 0.5)
    scene.addPointLight(pos, 40, Vec3(1, 1, 1))
    scene.build()

    width = 512
    height = 512
    n_samples = 10
    n_photons = 10
    n_estimation_global = 95
    n_photons_caustics_multiplier = 2
    n_estimation_caustics = 15
    final_gathering_depth = 4
    max_depth = 100

    image = Image(width, height)
    # coordinates must be in meters
    cam_pos = Vec3(0.2, 0.2, 0.4)
    camera = Camera(cam_pos, Vec3(0, 0.5, 0.5), 0.5 * PI)

    print("Building photonMap...")
    integrator = PhotonMapping(n_photons, n_estimation_global,
                               n_photons_caustics_multiplier, n_estimation_caustics,
                               final_gathering_depth, max_depth)

    sampler = UniformSampler(random.randint(1, sys.maxsize))

    integrator.build(scene, sampler)
    print("Done!")

    assert(integrator.getPhotonMap().nPhotons() >= 100)
if __name__ == "__main__":
    test_reflection()