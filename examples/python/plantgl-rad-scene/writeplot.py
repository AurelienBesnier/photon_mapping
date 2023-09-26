import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#TODO: Make a good plot

fig, ax = plt.subplots(layout='constrained')
width = 0.25  # the width of the bars
multiplier = 0

offset = width * multiplier
for band in ["400-500nm", "500-600nm", "600-700nm"]:
    filename = "captor_result-" + band + ".csv"

    df = pd.read_csv(filename)

    elevations = df.elevation.unique()
    photon_stats = {}

    for e in elevations:
        photon_stats[e] = 0

    for index, r in df.iterrows():
        photon_stats[r["elevation"]] += r["n_photons"]

    print(photon_stats)
    x = np.arange(len(elevations))  # the label locations

    keys = list(photon_stats.keys())
    values = list(photon_stats.values())

    for attribute, measurement in photon_stats.items():
        offset += width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=band)
    ax.bar_label(rects, padding=3)
    multiplier += 1

ax.set_title("Number of photon on elevation level of captor groups")
ax.set_xlabel('elevation')
ax.set_ylabel('n_photons')
ax.legend(loc='upper left', ncols=3)
plt.savefig("plot.png")
plt.close()
