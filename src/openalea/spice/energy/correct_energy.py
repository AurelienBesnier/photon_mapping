"""
Objective of this module is reading the measured PPFD of each wavelength to
correct the output energy.
Data is located in this directory: ./spectrum/chambre1_spectrum
"""

import re
from collections import OrderedDict

import pandas as pd
from scipy import stats

from openalea.spice.loader.load_sensor import findIndexOfDiskSensorInList


def read_spectrum_file(filename: str) -> (OrderedDict, int, int):
    """
    Parse a spectrum file.

    Parameters
    ----------
    filename: str
        The file to parse.

    Returns
    -------
    content: dict
        A dictionary with wavelength as key and photon count as value.
    step: int
        the step in the dictionary between two entries.
    start: int
        the first wavelength in the file.

    """
    content = OrderedDict()
    cpt_comment = 0

    with open(filename, encoding="UTF8") as f:
        lines = f.readlines()
        for line in lines:
            if line[0] != '"':  # ignore comment
                ls = re.split(r"\s+|;+", line, maxsplit=1)
                content[int(ls[0])] = float(ls[1].replace(",", "."))

            else:
                cpt_comment += 1
        first_line = re.split(r"\s+|;+", lines[cpt_comment], maxsplit=1)
        second_line = re.split(r"\s+|;+", lines[cpt_comment + 1], maxsplit=1)
        step = int(second_line[0]) - int(first_line[0])
    return content, step, int(first_line[0])


def get_integral_of_band(
    base_band: range, divided_band: range, spectrum: dict
) -> float:
    """
    Returns the integral of the band as a percentage.

    Parameters
    ----------
    base_band: range
        The base spectral range which includes all the other spectral ranges
    divided_band: range
        The section of the base spectral range used to run the simulation
    spectrum: dict
        The whole spectrum of the band.


    """
    sums = 0.0
    for i in divided_band:
        if i in spectrum:
            sums = sums + spectrum[i]

    total = 0.0
    for i in base_band:
        if i in spectrum:
            total = total + spectrum[i]

    return sums / total


def get_correct_energy_coeff(
    base_spectral_range, divided_spectral_range, spec_file: str
):
    """
    Get the coefficients of energy's correction from the spectrum file.

    Parameters
    ----------
    base_spectral_range: range
        The base spectral range which includes all the other spectral ranges
    divided_spectral_range: range
        The section of the base spectral range used to run the simulation
    spec_file: str
        The link to the file which contains the informations of the
        heterogeneity of the spectrum

    Returns
    -------
    integrals: array
        The list of the coefficents of energy's correction

    """

    spec_dict, _, _ = read_spectrum_file(spec_file)
    integrals = []
    base_band = range(base_spectral_range["start"], base_spectral_range["end"], 1)

    for _, spectral_range in enumerate(divided_spectral_range):
        divided_band = range(
            spectral_range["start"],
            spectral_range["end"],
            1,
        )

        integrals.append(get_integral_of_band(base_band, divided_band, spec_dict))

    return integrals


def get_points_calibration(
    list_sensors, points_calibration_file, divided_spectral_range
):
    """
    Read the file which contains the points used for the calibration.

    Parameters
    ----------
    list_sensors : array
        The list of sensors
    points_calibration_file: str
        The link to the file which contains the information of the captors used
        to calibrate the final result
    divided_spectral_range: array
        The list of spectral ranges divided from the base spectral range.

    Returns
    -------
    points_calibration: array
        The list of the points used for the calibration

    """

    points_calibration = []
    df = pd.read_csv(points_calibration_file)

    for _, value in enumerate(divided_spectral_range):
        cur_bande = value
        points = {}
        for _, r in df.iterrows():
            captor_index = findIndexOfDiskSensorInList(
                list_sensors, r["xSite"], r["ySite"], r["zSite"]
            )
            points[captor_index] = r[
                "Nmes_" + str(cur_bande["start"]) + "_" + str(cur_bande["end"])
            ]

        points_calibration.append(points)

    return points_calibration


def get_calibaration_coefficient(energies, correction_ratios, points_calibration):
    """
    Calculate the coefficients used to calibrate the result of simulation

    Parameters
    ----------
    energies : array
        The list of captor's energies
    correction_ratios: array
        The list of the coefficients of energy's correction
    points_calibration: array
        The list of the points used for the calibration

    Returns
    -------
    coeff_calibration: array
        The list of coefficients used for the calibration

    """

    coeff_calibration = []
    for i, energy in enumerate(energies):
        cur_points_calibration = points_calibration[i]

        # calculate N_sim appliqué le coefficient de correction
        n_sim_cor = {}
        for k, v in energy.items():
            n_sim_cor[k] = round(v * correction_ratios[i], 3)

        # regression linear
        n_mes_calibration = []
        n_sim_calibration = []

        for k, v in cur_points_calibration.items():
            n_sim_calibration.append(n_sim_cor[k])
            n_mes_calibration.append(v)

        slope, intercept, _, _, _ = stats.linregress(
            n_sim_calibration, n_mes_calibration
        )
        coeff_calibration.append({"slope": slope, "intercept": intercept})

    return coeff_calibration


def calibrate_captor_energy(
    energies, correction_ratios, points_calibration, coeffs_calibration
):
    """
    Calibrate the captor energy from photons to Mmol / m2 / s

    Parameters
    ----------
    energies : array
        The list of captor's energies
    correction_ratios: array
        The list of the coefficients of energy's correction
    points_calibration: array
        The list of the points used for the calibration
    coeffs_calibration : array
        The list of the coefficients used for the calibration

    Returns
    -------
    n_calibration: array
        The list of captor's energies after the calibration

    """
    n_calibration = []
    for i, energy in enumerate(energies):
        cur_coeffs_calibration = coeffs_calibration[i]
        cur_points_calibration = points_calibration[i]

        # calculate N_sim appliqué le coefficient de correction
        n_sim_cor = {}
        for k, v in energy.items():
            n_sim_cor[k] = round(v * correction_ratios[i], 3)

        # calculate Nmes
        n_mes_calculate = {}
        for k, v in n_sim_cor.items():
            if k in cur_points_calibration:
                n_mes_calculate[k] = cur_points_calibration[k]
            else:
                n_mes_calculate[k] = round(
                    cur_coeffs_calibration["slope"] * v
                    + cur_coeffs_calibration["intercept"],
                    5,
                )

        n_calibration.append(n_mes_calculate)

    return n_calibration


def calibrate_plant_energy(energies, coeffs_calibration):
    """
    Calibrate the plant energy from photons to Mmol / m2 / s

    Parameters
    ----------
    energies : array
        The list of captor's energies
    coeffs_calibration : array
        The list of the coefficients used for the calibration

    Returns
    -------
    n_calibration: array
        The list of plant's energies after the calibration

    """

    n_calibration = []
    for i, energy in enumerate(energies):
        cur_coeffs_calibration = coeffs_calibration[i]

        # calculate Nmes
        n_mes_calculate = {}
        for k, v in energy.items():
            n_mes_calculate[k] = round(
                cur_coeffs_calibration["slope"] * v
                + cur_coeffs_calibration["intercept"],
                5,
            )

        n_calibration.append(n_mes_calculate)

    return n_calibration
