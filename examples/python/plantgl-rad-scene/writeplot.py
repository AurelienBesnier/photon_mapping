import pandas as pd
import matplotlib.pyplot as plt

filename = "captor_result-435nm.csv"

df = pd.read_csv(filename)

print(df)

plt.plot(df["n_photons"], df["elevation"])
plt.savefig("plot.png")
