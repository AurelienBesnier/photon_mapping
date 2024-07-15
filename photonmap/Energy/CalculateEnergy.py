from collections import OrderedDict

#Objectif of this module is counting the number of photon on plant/captor
#Resultat is located in this directory: ./results

def write_captor_energy(energy, w_start, w_end, n_photons):
    od = OrderedDict(sorted(energy.items()))
    band = str(w_start) + "-" + str(w_end)

    filename = "results/captor_result-" + str(n_photons) + "-" + str(band) + "-nm.csv"

    with open(filename, "w") as f:
        f.write("id,n_photons,elevation\n")
        for k, v in od.items():
            if k <= 119:
                elevation = 1000
            elif k <= 239:
                elevation = 1400
            else:
                elevation = 1800
            print("captor n°" + str(k) + " has " + str(v) + " photons on it")
            f.write(str(k) + "," + str(v) + "," + str(elevation) + "\n")

    print("Done!")

def write_plant_energy(energy, w_start, w_end, n_photons):
    od = OrderedDict(sorted(energy.items()))
    band = str(w_start) + "-" + str(w_end)

    filename = "results/plant_result-" + str(n_photons) + "-" + str(band) + "-nm.csv"

    with open(filename, "w") as f:
        f.write("id,n_photons\n")
        for k, v in od.items():

            print("organes n°" + str(k) + " has " + str(v) + " photons on it")
            f.write(str(k) + "," + str(v) + "\n")

    print("Done!")

def captor_add_energy(captor_dict, integrator, energy):
    """
    Compute the energy on each captor in the scene.
    :param energy:
    :param captor_dict:
    :param integrator:
    :return:
    """
    photonmap = integrator.getPhotonMapCaptors()
    print(photonmap.nPhotons())
    print("writing captor energy...")
    for i in range(photonmap.nPhotons()):
        intersection = photonmap.getIthPhoton(i)
        captorId = captor_dict.get(intersection.triId)
        if captorId is None:
            print(captorId)

        if captorId is not None:  # check if the element hit is a captor
            if captorId in energy:
                energy[captorId] += 1
            else:
                energy[captorId] = 1


def compute_energy(tr2shmap, integrator):
    """
    Computes the number of photons on each organ of the plant.
    :param tr2shmap:
    :param integrator:
    :return:
    """
    photonmap = integrator.getPhotonMapCaptors()
    shenergy = {}
    for i in range(photonmap.nPhotons()):
        intersection = photonmap.getIthPhoton(i)
        triId = tr2shmap.get(intersection.triId)
        if triId is not None:  # check if the element hit is an element of the plant
            if triId in shenergy:
                shenergy[triId] += 1
            else:
                shenergy[triId] = 1

    for k, v in shenergy.items():
        print("organ n°" + str(k) + " has " + str(v) + " photons on it")
    
    return shenergy