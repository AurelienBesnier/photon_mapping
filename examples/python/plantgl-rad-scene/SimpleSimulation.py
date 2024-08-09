from photonmap.Simulator import *

if __name__ == "__main__":

    simulator = Simulator()

    #setup configuration
    simulator.nb_photons = 1000000
    simulator.max_depth = 5

    simulator.resetScene()
    #setup environment
    vert_ground = [(0,0,0), (1,0,0), (0,1,0)]
    ind_ground = [(0, 2, 1)]
    mat_ground = {
        "name": "Ground",
        "type": "object",
        "color": (0,0,0),
        "spec": 0.5,
        "roughness": 0,
        "trans": 0
    }
    simulator.addEnvToScene(vert_ground, ind_ground, mat_ground)

    #setup light
    vert_light = [(0,0,5), (1,0,5), (0,1,5)]
    ind_light = [(0, 1, 2)]
    mat_light = {
        "name": "Light",
        "type": "light",
        "color": (255, 255, 255)
    }
    simulator.addEnvToScene(vert_light, ind_light, mat_light)

    #setup captor
    simulator.addCaptorToScene((0.5, 0.5, 3), (0, 0, 1), 0.2)

    #run
    simulator.run()
