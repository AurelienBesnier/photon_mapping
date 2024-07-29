from collections import OrderedDict
from photonmap.Loader.LoadCaptor import Captor

#Objectif of this module is counting the number of photon on plant/captor
#Resultat is located in this directory: ./results

def write_captor_energy(N_sim, N_mes, captor_list, bands_spectre, n_photons):

    filename = "results/captor_result-" + str(n_photons) + ".csv"

    with open(filename, "w") as f:
        w_str = "id,xSite,ySite,zSite,radius"
        for i in range(len(bands_spectre)):
            w_str += ",N_mes_" + str(bands_spectre[i]["start"]) + "_" + str(bands_spectre[i]["end"])

        for i in range(len(bands_spectre)):
            w_str += ",N_sim_" + str(bands_spectre[i]["start"]) + "_" + str(bands_spectre[i]["end"])
        
        f.write(w_str + "\n")

        for k in range(len(captor_list)):
            captor = captor_list[k]
            w_str = str(k) + ',' + str(captor.xSite) + ',' + str(captor.ySite) + ',' + str(captor.zSite) + ',' + str(captor.radius)
            
            for i in range(len(bands_spectre)):
                cur_n_mes = N_mes[i]
                if k in cur_n_mes:
                    w_str += ',' + str(cur_n_mes[k])
                else:
                    w_str += ',' + str(0)

            for i in range(len(bands_spectre)):
                cur_n_sim = N_sim[i]
                if k in cur_n_sim:
                    w_str += ',' + str(cur_n_sim[k])
                else:
                    w_str += ',' + str(0)

            f.write(w_str + "\n")

    print("Done write captor energy!")

def write_plant_energy(energies, list_plant, bands_spectre, n_photons):
    filename = "results/plant_result-" + str(n_photons) + ".csv"

    with open(filename, "w") as f:
        w_str = "id"
        for i in range(len(bands_spectre)):
            w_str += ",N_sim_" + str(bands_spectre[i]["start"]) + "_" + str(bands_spectre[i]["end"])
        f.write(w_str + "\n")

        for sh_id in list_plant:
            w_str = str(sh_id)

            for i in range(len(bands_spectre)):
                cur_ener = energies[i]
                if sh_id in cur_ener:
                    w_str += ',' + str(cur_ener[sh_id])
                else:
                    w_str += ',' + str(0)
            f.write(w_str + "\n")

    print("Done write plant energy!")

def captor_add_energy(captor_dict, integrator, energy):
    """
    Compute the energy on each captor in the scene.
    :param energy:
    :param captor_dict:
    :param integrator:
    :return:
    """
    photonmap = integrator.getPhotonMapCaptors()
    
    print("writing captor energy...")
    for i in range(photonmap.nPhotons()):
        intersection = photonmap.getIthPhoton(i)
        captorId = captor_dict.get(intersection.triId)

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
    
    return shenergy