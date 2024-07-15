from photonmap.Simulator import *

if __name__ == "__main__":

    simulator = Simulator()
    simulator.readConfiguration("simulation.ini")
    simulator.setupRoom("./assets/testChamber.rad", "./PO")
    simulator.setupCaptor("./captors/captors_expe1.csv")
    #simulator.setupPlant("./assets/rose-simple4.lpy")
    simulator.run()

# command visualiser Environnement PlantGL
# ipython
# %gui qt
# run planglRadScene.py
