from scipy.integrate import simpson
from collections import OrderedDict
import re

#Objectif of this module is reading the measured PPFD of each wavelength to correct the output energy
#Data is located in this directory: ./spectrum/chambre1_spectrum

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
    with open(filename, "r") as f:
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

def get_integral_of_band(band: range, spectrum: dict) -> float:
    """
    Returns the integral of the band as a percentage
    Parameters
    ----------
    band: range
        The section of the spectrum to get.
    spectrum: dict
        The whole spectrum of the band.

    Returns
    -------

    """
    spec_range = []
    for i in band:
        if i in spectrum:
            spec_range.append(spectrum[i])
    
    I_simps = simpson(y=spec_range, x=None, axis=-1)

    return I_simps / 100  # get as percentage


def get_average_of_band(band: range, spectrum: dict) -> int:
    """
    Get the wavelength that represent the average of the count of photon send in a band of the spectrum of the light.
    Parameters
    ----------
    band: range
        The range of wavelength to compute the average of photon to send.
    spectrum: dict
        a dictionary representing the spectrum of the light with a wavelength as the key and a count of photons as the
        value.

    Returns
    -------
    wavelength: int
        The wavelength in question.
    """
    cpt: int = 0
    counts: float = 0.0
    b_dict: dict = {}
    for i in band:  # first for to get the average
        if i in spectrum:
            counts += spectrum[i]
            b_dict[i] = spectrum[i]
            cpt += 1

    avg = counts / cpt
    # get the closest wavelength of that average
    res_key, res_val = min(b_dict.items(), key=lambda x: abs(avg - x[1]))
    return res_key

def get_correct_energy_coeff(bands_spectre, spec_file : str):
    spec_dict, step, start = read_spectrum_file(spec_file)
    wavelengths = []
    integrals = []

    for index in range(len(bands_spectre)):
        r_band = range(bands_spectre[index]["start"], bands_spectre[index]["end"], 1)

        wavelengths.append(get_average_of_band(r_band, spec_dict))
        integrals.append(get_integral_of_band(r_band, spec_dict))

    
    return wavelengths, integrals

def correct_energy(shenergy: dict, correction_ratio):
    """
    Correct the energy computed during the simulation  with the integral of the chosen spectrum band.
    Parameters
    ----------
    shenergy: dict

    Returns
    -------

    """
    for k, v in shenergy.items():
        shenergy[k] = int(v * correction_ratio)