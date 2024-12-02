import os

# Objective of this module is counting the number of photon on plant/sensor
# Resultat is located in this directory: ./results


def write_sensor_energy(n_sim, n_calibration, sensor_list, bands_spectre, filename):
    """
    Write the received energy of all the sensors to a file.

    Parameters
    ----------
    n_sim : dict
        Number of received photons on each sensor
    n_calibration : dict
        The energies after the calibration on each sensor
    sensor_list : array
        The list of sensors
    bands_spectre: dict
        The divided spectral range used to run the simulation.
    filename: str
        The name of output file

    Returns
    -------
        A file with all the received energy of sensors saved in folder ./results

    """
    list_sensor_id = set()
    for k, sensor in enumerate(sensor_list):
        c_id = sensor.sensor_id
        list_sensor_id.add(c_id)

    os.makedirs("results", exist_ok=True)

    filename = "results/" + filename

    with open(filename, "w", encoding="UTF8") as f:
        w_str = "id"
        if len(n_calibration) == len(bands_spectre):
            for i, band in enumerate(bands_spectre):
                w_str += (
                    ",N_sim_calibration_" + str(band["start"]) + "_" + str(band["end"])
                )

        for i, band in enumerate(bands_spectre):
            w_str += ",N_sim_" + str(band["start"]) + "_" + str(band["end"])

        f.write(w_str + "\n")

        for k in list_sensor_id:
            w_str = str(k)
            # write result calibration
            if len(n_calibration) == len(bands_spectre):
                for i in range(len(bands_spectre)):
                    cur_n_calibration = n_calibration[i]
                    if k in cur_n_calibration:
                        w_str += "," + str(cur_n_calibration[k])
                    else:
                        w_str += "," + str(0)

            # write result simulation
            for i in range(len(bands_spectre)):
                cur_n_sim = n_sim[i]
                if k in cur_n_sim:
                    w_str += "," + str(cur_n_sim[k])
                else:
                    w_str += "," + str(0)

            f.write(w_str + "\n")

    print("Done write sensor energy!")


def sensor_add_energy(sensor_dict, integrator, energy):
    """
    Compute the energy on each sensor in the scene.

    Parameters
    ----------
    sensor_dict : dict
        The dictionary of sensor
    integrator: libphotonmap_core.PhotonMapping
        The object which handles all the simulation of photon mapping
    energy: dict
        The dictionary of sensor's energy

    """
    photonmap = integrator.getPhotonMapSensors()

    print("calculating sensor energy...")
    for i in range(photonmap.nPhotons()):
        intersection = photonmap.getIthPhoton(i)
        sensor_id = sensor_dict.get(intersection.triId)

        if sensor_id is not None:  # check if the element hit is a sensor
            if sensor_id in energy:
                energy[sensor_id] += 1
            else:
                energy[sensor_id] = 1
