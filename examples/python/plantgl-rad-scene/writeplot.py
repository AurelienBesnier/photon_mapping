import os

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re

# TODO: Make a good plot


width = 0.25  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

for file in os.listdir("./"):
    if file.startswith("captor_result"):
        df = pd.read_csv(file)
        m = re.findall(r"[^-]*", file)
        lw = m[4]
        hw = m[6]
        band = lw + "-" + hw + "nm"

        elevations = df.elevation.unique()
        photon_stats = {}

        for e in elevations:
            photon_stats[e] = 0

        for index, r in df.iterrows():
            photon_stats[r["elevation"]] += r["n_photons"]

        keys = [str(element) for element in photon_stats.keys()]
        values = list(photon_stats.values())

        # creating the bar plot
        plt.bar(keys, values)

        plt.title("Number of photon on elevation level of captor groups")
        plt.xlabel('elevation')
        plt.ylabel('n_photons')
        plt.savefig("plot" + band + ".png")

        plt.close()
