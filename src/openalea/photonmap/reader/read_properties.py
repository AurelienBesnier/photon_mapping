import os

import pandas as pd

from openalea.photonmap.energy.correct_energy import read_spectrum_file

# This module is read the optical properties (material) of each object
# Calculate the average value of the spectrum range


def setup_dataset_materials(w_start: int, w_end: int, po_dir: str):
    """
    Fills the materials_r (reflection), materials_s (specular) and materials_t
    (transmission) dictionaries with information from the provided data for the
    materials of the simulation.

    Parameters
    ----------
    w_start: int
        The first wavelength of band.
    w_end: int
        The last wavelength of band.
    po_dir: str
        The folder which contains all the optical properties of the room

    Returns
    -------
    materials_r : dict
        The reflections of all the materials
    materials_s : dict
        The specularities of all the materials
    materials_t : dict
        The transmission of all the materials

    """

    materials_t = {}
    materials_s = {}
    materials_r = {}

    for element in ("Plant", "Env"):  # Reflectances
        files = []
        dir_path_reflect = po_dir + "/" + element + "/ReflectancesMean/"

        if os.path.exists(dir_path_reflect):
            for path in os.listdir(dir_path_reflect):
                if os.path.isfile(os.path.join(dir_path_reflect, path)):
                    if not path.startswith("."):
                        files.append(path)
            for file in files:
                mat_name = file.split(".")[0]
                content_reflect, _, _ = read_spectrum_file(
                    os.path.join(dir_path_reflect, file)
                )

                refl = get_average_of_props_optic(
                    range(w_start, w_end, 1), content_reflect
                )

                materials_r[mat_name] = float(refl) if float(refl) > 0 else 0.0

    for element in ("Plant", "Env"):  # Transmittances
        files = []
        dir_path_transmit = po_dir + "/" + element + "/TransmittancesMean/"

        if os.path.exists(dir_path_transmit):
            for path in os.listdir(dir_path_transmit):
                if os.path.isfile(os.path.join(dir_path_transmit, path)):
                    if not path.startswith("."):
                        files.append(path)
            for file in files:
                mat_name = file.split(".")[0]
                content_transmit, _, _ = read_spectrum_file(
                    os.path.join(dir_path_transmit, file)
                )

                trans = get_average_of_props_optic(
                    range(w_start, w_end, 1), content_transmit
                )

                materials_t[mat_name] = float(trans) if float(trans) > 0 else 0.0

    # Specularities
    dir_path_spec = po_dir + "/Specularities.xlsx"

    if os.path.exists(dir_path_spec):
        content_spec = (
            pd.ExcelFile(dir_path_spec).parse(0)
            if dir_path_spec.endswith(".xlsx")
            else pd.read_csv(dir_path_spec)
        )
        mat_names = content_spec["Material"]
        mat_spec = content_spec["Visually estimated value"]

        for i, mat in enumerate(mat_spec):
            materials_s[mat_names[i]] = float(mat) if float(mat) > 0 else 0.0

    return materials_r, materials_s, materials_t


def get_average_of_props_optic(band: range, props: dict) -> float:
    """
    Calculate the average value of an optical property in a spectral range

    Parameters
    ----------
    band: range
        The spectral range which is considered
    props: dict
        A dictionary which contains the optical properties calculated for each
        wavelength in spectral range

    Returns
    -------
        result: float
            the average optical property in a spectral range
    """

    res = 0.0
    count = 0
    for i in band:
        if i in props:
            res += props[i]
            count += 1

    if count != 0:
        res /= count

    return res
