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

| To setup the captors (The objects that we do the calculations of light's energy), we have to define its geometry, material and position
| The optical properties of captor's material are the same as the optical properties of environment's material
| In this tools, we have 2 type of captors:
| - ``FaceCaptor``: the material of this captor work like the material of the other surfaces 
| - ``VirtualCaptor``: the material of this captor has no effect to the light in the simulation

.. code-block:: python
    
    #setup captor
    captor_ts = TriangleSet(pointList = [(0,0,1), (1,0,0), (0,1,0)], indexList = [(0, 1, 2)])
    captor_mat = Material(
                            name="Captor",
                            ambient = Color3( 127 ),
                            specular = Color3( 127 ), #spec = 0.5 = 127/255
                            shininess = 0.5,
                            transparency = 0.5
                        )
    captor_sh = Shape(captor_ts, captor_mat, 0)

    simulator.addFaceCaptorToScene(shape=captor_sh, position=(0,0,3), scale_factor=1)
    simulator.addVirtualCaptorToScene(shape=captor_sh, position=(0,0,2), scale_factor=1)

To run the simulation, we use the function ``run`` of the object ``Simulator``. The result of the simulation is saved in an object of type ``SimulationResult``

.. code-block:: python

    #run
    res = simulator.run()

| To write the result to a file, using the function ``writeResults`` of the object ``SimulationResult``

.. code-block:: python
    
    #write result to file
    res.writeResults("filename")

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
        captor_ts = TriangleSet(pointList = [(0,0,1), (1,0,0), (0,1,0)], indexList = [(0, 1, 2)])
        captor_mat = Material(
                            name="Captor",
                            ambient = Color3( 127 ),
                            specular = Color3( 127 ), #spec = 0.5 = 127/255
                            shininess = 0.5,
                            transparency = 0.5
                        )
        captor_sh = Shape(captor_ts, captor_mat, 0)
        simulator.addFaceCaptorToScene(shape=captor_sh, position=(0,0,3), scale_factor=1)
        simulator.addVirtualCaptorToScene(shape=captor_sh, position=(0,0,2), scale_factor=1)
    
        #run
        res = simulator.run()
        res.writeResults()
