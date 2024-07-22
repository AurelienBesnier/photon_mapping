from photonmap import Vec3
import sys, os
#This module consist the common functions using in this project 

def wavelength2Rgb(w: int) -> Vec3:
    """
    Convert a wavelength between 400 - 800 nm to RGB color
    Parameters
    ----------
    w: int
        The wavelength to convert

    Returns
    -------
    RGB: Vec3
        A Vec3 structure representing an RGB color.

    """
    if 380.0 <= w < 440:
        red = -(w - 440.0) / (440.0 - 380.0)
        green = 0.0
        blue = 1.0
    elif 440.0 <= w < 490.0:
        red = 0.0
        green = (w - 440.0) / (490.0 - 440.0)
        blue = 1.0
    elif 490.0 <= w < 510.0:
        red = 0.0
        green = 1.0
        blue = -(w - 510.0) / (510.0 - 490.0)
    elif 510.0 <= w < 580.0:
        red = (w - 510.0) / (580.0 - 510.0)
        green = 1.0
        blue = 0.0
    elif 580.0 <= w < 645.0:
        red = 1.0
        green = -(w - 645.0) / (645.0 - 580.0)
        blue = 0.0
    elif 645.0 <= w < 781.0:
        red = 1.0
        green = 0.0
        blue = 0.0
    else:
        red = 0.0
        green = 0.0
        blue = 0.0

    return photonmap.Vec3(red, green, blue)


def flatten(lt: list) -> list:
    """
    Flattens a list
    Parameters
    ----------
    lt: list
        a list

    Returns
    ---------
    l: list
        the flattened list

    """
    return [item for sublist in lt for item in sublist]


def blockPrint():

    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():

    sys.stdout = sys.__stdout__