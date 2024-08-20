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

| Setup light and environment by using the object Shape of openalea
|
| In general, we can setup the environment and light with the same function ``addEnvToScene``. However, the ways that we define the material of object will identify the type of object is environment or light.
|
| For the environment, there are 4 optical properties which is need to be declared:
| - ambient: The reflection of object
| - specular: The specular of object
| - shininess: The shininess of object. The roughness of object is equal to ``1 - shininess``
| - transparency: The transparent of object
|
| For the light source, only the ``emission`` need to be declared. This value is also the different between these two type of object.

.. code-block:: python

    simulator.resetScene()
    #setup environment
    ground_ts = TriangleSet(pointList = [(0,0,0), (1,0,0), (0,1,0)], indexList = [(0, 2, 1)])
    ground_mat = Material(
                        name="Ground",
                        ambient = Color3(0),
                        specular = Color3(127), #spec = 0.5 = 127/255
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

| Setup captors and run by defining its geometry and position

.. code-block:: python
    
    #setup captor
    captor_ts = TriangleSet(pointList = [(0,0,1), (1,0,0), (0,1,0)], indexList = [(0, 1, 2)])
    simulator.addCaptorToScene(captor_ts, (0,0,3))

    #run
    res = simulator.run()

| To write the result to a file, using the function ``writeResults`` after the function ``run``

.. code-block:: python
    
    #write result to file
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
                            emission = Color3(255, 255, 255)
                        )
        light_sh = Shape(light_ts, light_mat)
        simulator.addEnvToScene(light_sh)

        #setup captor
        captor_ts = TriangleSet(pointList = [(0,0,1), (1,0,0), (0,1,0)], indexList = [(0, 1, 2)])
        simulator.addCaptorToScene(captor_ts, (0,0,3))

        #run
        res = simulator.run()
        simulator.writeResults()
