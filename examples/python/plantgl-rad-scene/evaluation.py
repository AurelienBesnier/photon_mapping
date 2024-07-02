import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re

fig, ax = plt.subplots(layout='constrained')
dir = "./results/res/"
for file in os.listdir(dir):
    if file.startswith("captor_result"):
        print(file)
        df = pd.read_csv(dir + file)
        m = re.findall(r"[^-]*", file)
        lw = m[4]
        hw = m[6]
        band = lw + "-" + hw + "nm"

     
        values = []
        keys = []

        for index, r in df.iterrows():
            values.append(r["n_photons"])
            keys.append(index)

        # creating the bar plot
        plt.scatter(keys, values)

        plt.title("Result of wavelength " + band)
        plt.xlabel('captors')
        plt.ylabel('n_photons')
        plt.savefig("plot" + band + ".png")

        plt.close()