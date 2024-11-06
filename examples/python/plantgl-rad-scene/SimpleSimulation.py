from openalea.photonmap.Simulator import *
from openalea.plantgl.all import * 

if __name__ == "__main__":

    simulator = Simulator()

    #setup configuration
    simulator.nb_photons = 1000000
    simulator.max_depth = 5
    simulator.resetScene()

    #setup environment
    ground_ts = TriangleSet(pointList = [(0,0,0), (1,0,0), (0,1,0)], indexList = [(0, 1, 2)])
    ground_mat = Material(
                        name="Ground",
                        ambient = Color3( 0 ),
                        specular = Color3( 127 ), #spec = 0.5 = 127/255
                        shininess = 1,
                        transparency = 0
                    )
    ground_sh = Shape(ground_ts, ground_mat)

    simulator.addEnvToScene(ground_sh)

    #setup light
    light_ts = TriangleSet(pointList = [(0,0,5), (1,0,5), (0,1,5)], indexList = [(0, 1, 2)])
    light_mat = Material(
                        name="Light",
                        emission = Color3(255, 255, 255)
                    )
    light_sh = Shape(light_ts, light_mat)
    simulator.addEnvToScene(light_sh)

    #setup captor
    captor_ts = TriangleSet(pointList = [(0,0,0), (1,0,0), (0,1,0)], indexList = [(0, 2, 1)])
    captor_mat = Material(
                        name="Captor",
                        ambient = Color3( 127 ),
                        specular = Color3( 127 ), #spec = 0.5 = 127/255
                        shininess = 0.5,
                        transparency = 0.5
                    )
    captor_sh = Shape(captor_ts, captor_mat, 0)

    #simulator.addFaceCaptorToScene(shape=captor_sh, position=(0,0,1), scale_factor=1)
    simulator.addVirtualCaptorToScene(shape=captor_sh, position=(0,0,3), scale_factor=1)

    #run
    res = simulator.run()
    res.writeResults()