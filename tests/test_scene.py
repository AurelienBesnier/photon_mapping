from photonmap import Scene


def test_load_scene_with_lights():
    scene = Scene()
    scene.loadModel("./tests/cornellbox-water2.obj")
    scene.build()
    assert scene.nLights() == 2
