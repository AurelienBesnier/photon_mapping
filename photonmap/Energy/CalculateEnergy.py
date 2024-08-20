from collections import OrderedDict
from photonmap.Loader.LoadCaptor import Captor
import os

#Objectif of this module is counting the number of photon on plant/captor
#Resultat is located in this directory: ./results

def write_captor_energy(N_sim, N_calibration, captor_list, bands_spectre, n_photons):
    """
    Write the received energy of all the captors to a file.

    Parameters
    ----------
    N_sim : dict
        Number of received photons on each captor
    N_calibration : dict
        The energies after the calibration on each captor
    captor_list : array
        The list of captors
    bands_spectre: dict
        The divided spectral range used to run the simulation.
    nb_photons: int
        The number of photons in simulation

    Returns
    -------
        A file with all the received energy of captors saved in folder ./results

    """

    if not os.path.exists("results"):
        os.makedirs("results")

    filename = "results/captor_result-" + str(n_photons) + ".csv"

    with open(filename, "w") as f:
        w_str = "id,geometry_type,xSite,ySite,zSite,radius"

        if len(N_calibration) == len(bands_spectre):
            for i in range(len(bands_spectre)):
                w_str += ",N_sim_calibration_" + str(bands_spectre[i]["start"]) + "_" + str(bands_spectre[i]["end"])

        for i in range(len(bands_spectre)):
            w_str += ",N_sim_" + str(bands_spectre[i]["start"]) + "_" + str(bands_spectre[i]["end"])
        
        f.write(w_str + "\n")

        for k in range(len(captor_list)):
            captor = captor_list[k]
            w_str = str(k) + ',' + captor.type + ',' + str(captor.xSite) + ',' + str(captor.ySite) + ',' + str(captor.zSite) + ',' + str(captor.radius)  
            
            #write result calibration
            if len(N_calibration) == len(bands_spectre):
                for i in range(len(bands_spectre)):
                    cur_N_calibration = N_calibration[i]
                    if k in cur_N_calibration:
                        w_str += ',' + str(cur_N_calibration[k])
                    else:
                        w_str += ',' + str(0)

            #write result simulation
            for i in range(len(bands_spectre)):
                cur_n_sim = N_sim[i]
                if k in cur_n_sim:
                    w_str += ',' + str(cur_n_sim[k])
                else:
                    w_str += ',' + str(0)

            f.write(w_str + "\n")

    print("Done write captor energy!")

def write_plant_energy(energies, N_calibration, list_plant, bands_spectre, n_photons):
    """
    Write the received energy of all the organs of plant to a file.

    Parameters
    ----------
    energies : dict
        Number of received photons on each plant's organs
    N_calibration : dict
        The energies after the calibration on each plant's organs
    list_plant : dict
        The dictionary of plant's organs
    bands_spectre: dict
        The divided spectral range used to run the simulation.
    nb_photons: int
        The number of photons in simulation

    Returns
    -------
        A file with all the received energy of plant's organs saved in folder ./results

    """

    if not os.path.exists("results"):
        os.makedirs("results")
        
    filename = "results/plant_result-" + str(n_photons) + ".csv"

    with open(filename, "w") as f:
        w_str = "id"

        if len(N_calibration) == len(bands_spectre):
            for i in range(len(bands_spectre)):
                w_str += ",N_sim_calibration_" + str(bands_spectre[i]["start"]) + "_" + str(bands_spectre[i]["end"])

        for i in range(len(bands_spectre)):
            w_str += ",N_sim_" + str(bands_spectre[i]["start"]) + "_" + str(bands_spectre[i]["end"])

        f.write(w_str + "\n")

        for sh_id in list_plant:
            w_str = str(sh_id)

            #write result calibration
            if len(N_calibration) == len(bands_spectre):
                for i in range(len(bands_spectre)):
                    cur_N_calibration = N_calibration[i]
                    if sh_id in cur_N_calibration:
                        w_str += ',' + str(cur_N_calibration[sh_id])
                    else:
                        w_str += ',' + str(0)

            #write result simulation
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

    Parameters
    ----------
    captor_dict : dict
        The dictionary of captor
    integrator: libphotonmap_core.PhotonMapping
        The object which handles all the simulation of photon mapping
    energy: dict
        The dictionary of captor's energy

    """
    photonmap = integrator.getPhotonMapCaptors()
    
    print("calculating captor energy...")
    for i in range(photonmap.nPhotons()):
        intersection = photonmap.getIthPhoton(i)
        captorId = captor_dict.get(intersection.triId)

        if captorId is not None:  # check if the element hit is a captor
            if captorId in energy:
                energy[captorId] += 1
            else:
                energy[captorId] = 1


def plant_add_energy(tr2shmap, integrator):
    """
    Computes the number of photons on each organ of the plant.

    Parameters
    ----------
    tr2shmap : dict
        The dictionary of plant's organs
    integrator: libphotonmap_core.PhotonMapping
        The object which handles all the simulation of photon mapping

    Returns
    -------
    shenergy: dict
        The dictionary of plant's energy

    """
    photonmap = integrator.getPhotonMapCaptors()
    
    print("calculating plant energy...")
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