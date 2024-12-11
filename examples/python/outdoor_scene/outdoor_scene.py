import openalea.plantgl.all as pgl
from openalea.spice.simulator import Simulator
from openalea.spice import Vec3

pgl_scene = pgl.Scene('./Ind_1_TT_900L.obj')

sim = Simulator()
sim.configuration.NB_PHOTONS = 10000
sim.configuration.SCALE_FACTOR = 0.1
sim.configuration.MAXIMUM_DEPTH = 50
for sh in pgl_scene:
    sim.addFaceSensor(sh)



sim.addPointLight(Vec3(0,5,0), 100000)
sim.run()

sim.visualizePhotons('ipython')
