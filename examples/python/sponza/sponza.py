import openalea.plantgl.all as pgl
from openalea.spice.simulator import Simulator
from openalea.spice import Vec3
from pathlib import Path

pgl_scene = pgl.Scene(str(Path.home() / 'models/Sponza/sponza.obj'))

sim = Simulator()
sim.configuration.NB_PHOTONS = 100000
sim.configuration.SCALE_FACTOR = 1
sim.configuration.MAXIMUM_DEPTH = 50
print(f"nb shapes {len(pgl_scene)}")
i=0
for sh in pgl_scene:
    print("\033[A\33[2K\r", end="")
    print(f"Adding shape {i}/{len(pgl_scene)}")
    sim.addFaceSensor(sh)
    i+=1

sim.scene_pgl = pgl_scene


sim.addPointLight(Vec3(0,10,0), 100000)
sim.run()

sim.visualizePhotons('ipython')
