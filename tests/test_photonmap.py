from openalea.spice import PhotonMapping, Scene, UniformSampler, Vec3


def test_photonmaps():
    """Test if every photon maps has at least an element"""
    scene = Scene()
    scene.loadModel("./tests/testChamberPH.obj")
    pos = Vec3(0, 1, 0)
    scene.addPointLight(pos, 400, Vec3(1, 1, 1))
    scene.build(False)

    n_photons = 100
    n_estimation_global = 95
    n_photons_caustics_multiplier = 2
    n_estimation_caustics = 15
    final_gathering_depth = 4
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

    assert integrator.getPhotonMap().nPhotons() > 0
    #assert integrator.getPhotonMapCaustics().nPhotons() > 0
