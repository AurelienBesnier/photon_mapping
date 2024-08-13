Code example
##############

| Create a simple simulation without using the input files.

| Import the library and create an object Simulator

.. code-block:: python

    from photonmap.Simulator import *

    if __name__ == "__main__":
        simulator = Simulator()
        

| Setup configuration

.. code-block:: python

    #setup configuration
    simulator.nb_photons = 1000000
    simulator.max_depth = 5

| Setup light and environment

.. code-block:: python

    simulator.resetScene()
    #setup environment
    ground_ts = TriangleSet(pointList = [(0,0,0), (1,0,0), (0,1,0)], indexList = [(0, 2, 1)])
    ground_mat = Material(
                        name="Ground",
                        ambient = Color3(0,0,0),
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
                        ambient = Color3(255, 255, 255),
                        emission = Color3(255, 255, 255)
                    )
    light_sh = Shape(light_ts, light_mat)
    simulator.addEnvToScene(light_sh)

| Setup captors and run

.. code-block:: python
    
    #setup captor
    simulator.addCaptorToScene((0.5, 0.5, 3), (0, 0, 1), 0.2)

    #run
    simulator.run()

| To write the result to a file, using the function ``writeResults`` after the function ``run``

.. code-block:: python
    
    #write result to file
    res = simulator.run()
    simulator.writeResults()

| Here is the completed program

.. code-block:: python

    from photonmap.Simulator import *
    from openalea.plantgl.all import * 

    if __name__ == "__main__":

        simulator = Simulator()

        #setup configuration
        simulator.nb_photons = 1000000
        simulator.max_depth = 5

        simulator.resetScene()

        #setup environment
        ground_ts = TriangleSet(pointList = [(0,0,0), (1,0,0), (0,1,0)], indexList = [(0, 2, 1)])
        ground_mat = Material(
                            name="Ground",
                            ambient = Color3(0,0,0),
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
                            ambient = Color3(255, 255, 255),
                            emission = Color3(255, 255, 255)
                        )
        light_sh = Shape(light_ts, light_mat)
        simulator.addEnvToScene(light_sh)

        #setup captor
        simulator.addCaptorToScene((0.5, 0.5, 3), (0, 0, 1), 0.2)

        #run
        res = simulator.run()
        simulator.writeResults()
