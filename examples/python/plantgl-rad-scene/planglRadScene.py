from photonmap.Simulator import *

if __name__ == "__main__":

    simulator = Simulator()
    simulator.readConfiguration("simulation.ini")
    simulator.setupRoom("./assets/testChamber.rad", "./PO")
    #simulator.setupCaptor("./captors/captors_expe1.csv")
    simulator.setupCaptor("./captors/captors_expe1.csv", "spectrum/chambre1_spectrum", "points_calibration.csv")
    #simulator.setupRender(Vec3(1280.0, 300.0, 1500.0), Vec3(1280.0, 860.0, 980.0))
    #simulator.setupPlant("./assets/rose-simple4.lpy", Vec3(1280.0, 860.0, 980.0))
    simulator.run()
    #simulator.test_t_min(int(1e6), 1e-6, 10, True)

    #simulator.visualiserSimulationScene()

# command visualiser Environnement PlantGL
# ipython
# %gui qt
# run planglRadScene.py
