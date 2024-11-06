import os

# Objectif of this module is counting the number of photon on plant/captor
# Resultat is located in this directory: ./results


def write_captor_energy(N_sim, N_calibration, captor_list, bands_spectre, filename):
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
    filename: str
        The name of output file

    Returns
    -------
        A file with all the received energy of captors saved in folder ./results

    """
    list_captor_id = set()
    for k in range(len(captor_list)):
        c_id = captor_list[k].captor_id
        list_captor_id.add(c_id)

    if not os.path.exists("results"):
        os.makedirs("results")

    filename = "results/" + filename

    with open(filename, "w") as f:
        w_str = "id"
        if len(N_calibration) == len(bands_spectre):
            for i in range(len(bands_spectre)):
                w_str += (
                    ",N_sim_calibration_"
                    + str(bands_spectre[i]["start"])
                    + "_"
                    + str(bands_spectre[i]["end"])
                )

        for i in range(len(bands_spectre)):
            w_str += (
                ",N_sim_"
                + str(bands_spectre[i]["start"])
                + "_"
                + str(bands_spectre[i]["end"])
            )

        f.write(w_str + "\n")

        for k in list_captor_id:
            w_str = str(k)
            # write result calibration
            if len(N_calibration) == len(bands_spectre):
                for i in range(len(bands_spectre)):
                    cur_N_calibration = N_calibration[i]
                    if k in cur_N_calibration:
                        w_str += "," + str(cur_N_calibration[k])
                    else:
                        w_str += "," + str(0)

            # write result simulation
            for i in range(len(bands_spectre)):
                cur_n_sim = N_sim[i]
                if k in cur_n_sim:
                    w_str += "," + str(cur_n_sim[k])
                else:
                    w_str += "," + str(0)

            f.write(w_str + "\n")

    print("Done write captor energy!")


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
