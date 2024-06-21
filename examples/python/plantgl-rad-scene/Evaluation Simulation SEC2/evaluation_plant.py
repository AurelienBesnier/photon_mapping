import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re


def read_resultat_plant(file: str):
    ids = []
    photons = []
    df = pd.read_csv(file)
    for index, r in df.iterrows():
        ids.append(r["id"])
        photons.append(r["n_photons"])
    
    return ids, photons

if __name__ == "__main__":
    
    ids, photons = read_resultat_plant("res_final/captor_result-1000000000-655-665-nm_plant.csv")
    
    
    plt.plot(ids, photons, linestyle='--', marker='o', color='b')
    
    plt.title("Wavelength 655-665 nm / Distribution des photons sur des organes du plant")
    plt.ylabel("Nb of photon")
    plt.xlabel("Index d'organes")
    plt.show()
    
