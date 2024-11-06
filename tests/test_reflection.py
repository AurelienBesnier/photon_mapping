from openalea.photonmap import PhotonMapping, Scene, UniformSampler, Vec3


def test_reflection():
    """Test if photon from a light source all
    end up on an absorbing surface."""
    scene = Scene()
    scene.loadModel("./tests/testChamberPH.obj")
    pos = Vec3(0, 1, 0)
    scene.addPointLight(pos, 400, Vec3(1, 1, 1))
    scene.build()

    n_photons = 100
    n_estimation_global = 95
    n_photons_caustics_multiplier = 2
    n_estimation_caustics = 15
    final_gathering_depth = 0
    max_depth = 100

    print("Building photonMap...")
    integrator = PhotonMapping(
        n_photons,
        n_estimation_global,
        n_photons_caustics_multiplier,
        n_estimation_caustics,
        final_gathering_depth,
        max_depth,
    )

    sampler = UniformSampler(1)

    integrator.build(scene, sampler, True)
    print("Done!")

    assert integrator.getPhotonMap().nPhotons() >= 50
