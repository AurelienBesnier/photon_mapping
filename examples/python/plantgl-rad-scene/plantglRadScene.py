from openalea.spice.simulator import Simulator

if __name__ == "__main__":

    simulator = Simulator(config_file="simulation.ini")
    simulator.addVirtualDiskSensorsFromFile("./captors/captors_expe1.csv")

    # simulator.setupRender(Vec3(68.0, 1200.0, 1500.0), Vec3(1280.0, 860.0, 980.0), 75.0)
    # simulator.n_samples = 2
    res = simulator.run()

    simulator.visualizeResults()

# command visualiser Environnement PlantGL
# ipython
# %gui qt
# run planglRadScene.py
