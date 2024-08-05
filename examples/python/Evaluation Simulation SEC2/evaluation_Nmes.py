import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re


def read_resultat_nmes(file: str):
    ids = []
    nmes_600_655 = []
    nmes_655_665 = []
    df = pd.read_csv(file)
    for index, r in df.iterrows():
        ids.append(r["id"])
        nmes_600_655.append(r["N_mes_600_655"])
        nmes_655_665.append(r["N_mes_655_665"])
    
    return ids, nmes_600_655, nmes_655_665
    
def read_prop_optique(file: str):
    _lambda = []
    val = []
    df = pd.read_csv(file)
    for index, r in df.iterrows():
        _lambda.append(r["lambda"])
        val.append(r["moy"])
    
    return _lambda, val

if __name__ == "__main__":
   
    
    xls = pd.ExcelFile(r"simuMesureExpes12_tout.xls") # use r before absolute file path 

    res_simulation = xls.parse(0) #2 is the sheet number+1 thus if the file has only 1 sheet write 0 in paranthesis
    res_captor_rayon = res_simulation['rayonCapteur']
    res_600_655 = res_simulation['600_655_mumolM2S_mes']
    res_655_665 = res_simulation['655_665_mumolM2S_mes']
    
    res_sec2_600_655 = []
    res_sec2_655_665 = []
    for i in range(len(res_600_655)):
    	if (res_captor_rayon[i] == 10):
    	   res_sec2_600_655.append(res_600_655[i])
    	   res_sec2_655_665.append(res_655_665[i])
    
    ids, cur_mes_600_655, cur_mes_655_665 = read_resultat_nmes("captor_result-1000000000.csv")
    
    z3 = np.polyfit(res_sec2_600_655, cur_mes_600_655, 1)
    p3 = np.poly1d(z3)
    plt.scatter(res_sec2_600_655, cur_mes_600_655, 20, 'b')
    plt.plot(res_sec2_600_655, p3(res_sec2_600_655), 'r')
    plt.title("Wavelength 600-655 nm / Mmol par m² par s ")
    plt.ylabel("Current res")
    plt.xlabel("Res sec2")
    plt.show()


    
