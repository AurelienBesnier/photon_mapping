import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re

def read_sec2_resultat(file: str):
    res_sec2 = []
    with open(file, "r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            if(lines[i].startswith("nb particules")):
                li = lines[i].split(None)
                nb_photon = int(li[3])
                res_sec2.append(nb_photon)
        
        return res_sec2

def read_current_resultat(file: str):
    res_current_1000 = []
    res_current_1400 = []
    
    df = pd.read_csv(file)
    for index, r in df.iterrows():
        if r["elevation"] == 1000:
            res_current_1000.append(r["n_photons"])
        else:
            res_current_1400.append(r["n_photons"])
    
    return res_current_1000, res_current_1400

def read_resultat_plant(file: str):
    id = []
    photons = []
    df = pd.read_csv(file)
    for index, r in df.iterrows():
        id.append(r[id])
        photons.append(r[n_photons])
    
    return id, photons

if __name__ == "__main__":
    res_sec2 = read_sec2_resultat("res_sec2/mesures.txt")
    res_current_1000, res_current_1400 = read_current_resultat("res_final/captor_result-1000000000-655-665-nm.csv")
    res_cur = res_current_1000 + res_current_1400
    
    res_sec2 = read_sec2_resultat("res_sec2/mesures.txt")
    res_old_1000, res_old_1400 = read_current_resultat("res_final/captor_result-1000000000-655-665-nm_ancien.csv")
    res_old = res_old_1000 + res_old_1400
	    
    res_cor_diffuse_1000, res_cor_diffuse_1400 = read_current_resultat("res_final/captor_result-1000000000-655-665-nm_correctDiffuse.csv")
    res_cor_diffuse = res_cor_diffuse_1000 + res_cor_diffuse_1400
    
    res_cor_tnear_1000, res_cor_tnear_1400 = read_current_resultat("res_final/captor_result-1000000000-655-665-nm_correctTnear.csv")
    res_cor_tnear = res_cor_tnear_1000 + res_cor_tnear_1400
    
    res_cor_captor_dir_1000, res_cor_captor_dir_1400 = read_current_resultat("res_final/captor_result-1000000000-655-665-nm_BackfaceCaptor.csv")
    res_cor_captor_dir = res_cor_captor_dir_1000 + res_cor_captor_dir_1400
    
    res_cor_captor_geo_1000, res_cor_captor_geo_1400 = read_current_resultat("res_final/captor_result-1000000000-655-665-nm.csv")
    res_cor_captor_geo = res_cor_captor_geo_1000 + res_cor_captor_geo_1400
    
    res_cor_illum_1000, res_cor_illum_1400 = read_current_resultat("res_final/captor_result-1000000000-655-665-nm_correctIllumination.csv")
    res_cor_illum = res_cor_illum_1000 + res_cor_illum_1400
    
    res_lcg_1000, res_lcg_1400 = read_current_resultat("res_final/captor_result-1000000000-655-665-nm_RAND.csv")
    res_lcg = res_lcg_1000 + res_lcg_1400
    
    res_xoroshiro_1000, res_xoroshiro_1400 = read_current_resultat("res_final/captor_result-1000000000-655-665-nm_xoroshiro.csv")
    res_xoroshiro = res_xoroshiro_1000 + res_xoroshiro_1400
    
    res_splitmix_1000, res_splitmix_1400 = read_current_resultat("res_final/captor_result-1000000000-655-665-nm_SplitMix.csv")
    res_splitmix = res_splitmix_1000 + res_splitmix_1400
    
    #x = range(0, len(res_sec2))
    #plt.plot(x, res_sec2, 'r')
    #plt.plot(x, res_cur, 'g')
    #plt.legend(["Resultat SEC2", "Current resultat"])
    #plt.title("Wavelength 655-665 nm / Après de modifier la géométrie de captor")
    #plt.ylabel("Nb of photon")
    #plt.xlabel("Index of captor")
    #plt.show()
    
    res_dif = [
    	# Correct Bug
    	#np.subtract(res_cor_diffuse, res_sec2),
    	#np.subtract(res_cor_tnear, res_sec2),
    	#np.subtract(res_cor_captor_dir, res_sec2),
    	#np.subtract(res_cor_captor_geo, res_sec2)
  	np.subtract(res_cor_captor_dir, res_sec2),
  	np.subtract(res_cor_captor_geo, res_sec2)
    	
    	#PRNG test
    	#np.subtract(res_cur, res_sec2),
    	#np.subtract(res_lcg, res_sec2),
    	#np.subtract(res_splitmix, res_sec2),
    	#np.subtract(res_xoroshiro, res_sec2)
    ]
    labels = [
    	# Correct Bug
    	#"Correct Diffuse & Speculaire", 
    	#"Correct Tnear", 
    	#"Correct Back-face Culling", 
    	#"Correct Captor Geo", 
    	
    	
    	"Ignorer les faces arrière",
    	"Modifier la géométrie de capteur"
    	
    	# PRNG test
    	#"PCG", 
    	#"LCG", 
    	#"SplitMix", 
    	#"Xoroshiro"
    ]
    
    #plt.title("La différence entre le résultat de notre moteur et SEC2")
    #plt.ylabel("Nb of photon")
    #plt.boxplot(res_dif, patch_artist=False, labels=labels)
    #plt.show()

    #x = ["PCG", "LCG", "SplitMix", "Xoroshiro"]
    #y = [288.5, 292.2, 298.1, 291.8]
    #plt.bar(x, y)
    #plt.title("Performance according to PRNG")
    #plt.ylabel("Times (s)")
    #plt.xlabel("Pseudo random number generator")
    #plt.show()
    
    x = [1,2,4,8]
    #y = [1298.5, 662.6, 346.4, 263.72]
    y = [1442.3, 734.8, 380.4, 286.3]
    plt.plot(x, y, '-s')
    plt.title("Performances avec des différents nombre de threads")
    plt.ylabel("Temps (s)")
    plt.xlabel("Nombre de threads")
    plt.show()
    
    #x = ["SEC2", "Notre moteur original", "Notre moteur courrant"]
    #y = [2113, 1264, 286]
    #plt.bar(x, y)
    #plt.title("Performance de chaque version de moteur")
    #plt.ylabel("Temps (s)")
    #plt.xlabel("Version de moteur")
    #plt.show()

    # xls = pd.ExcelFile(r"simuMesureExpes12_tout.xls") # use r before absolute file path 

    # res_simulation = xls.parse(0) #2 is the sheet number+1 thus if the file has only 1 sheet write 0 in paranthesis

    # res_captor_rayon = res_simulation['rayonCapteur']
    # res_captor_hauteur = res_simulation['zSite']
    # res_400_445 = res_simulation['400_445_cptNormM2_sim']
    # res_445_455 = res_simulation['445_455_cptNormM2_sim']
    # res_455_500 = res_simulation['455_500_cptNormM2_sim']
    # res_500_534 = res_simulation['500_534_cptNormM2_sim']
    # res_534_542 = res_simulation['534_542_cptNormM2_sim']
    # res_542_600 = res_simulation['542_600_cptNormM2_sim']
    # res_600_655 = res_simulation['600_655_cptNormM2_sim']
    # res_655_665 = res_simulation['655_665_cptNormM2_sim']
    # res_665_700 = res_simulation['665_700_cptNormM2_sim']
    # res_700_725 = res_simulation['700_725_cptNormM2_sim']
    # res_725_735 = res_simulation['725_735_cptNormM2_sim']
    # res_735_800 = res_simulation['735_800_cptNormM2_sim']


    # res_exp_1_1000 = {
    #     '400_445': [],
    #     '655_665': [],
    #     '735_800': []
    # }

    # res_exp_1_1400 = {
    #     '400_445': [],
    #     '655_665': [],
    #     '735_800': []
    # }

    # cur_res_exp_1_1000 = {
    #     '400_445': [],
    #     '655_665': [],
    #     '735_800': []
    # }

    # cur_res_exp_1_1400 = {
    #     '400_445': [],
    #     '655_665': [],
    #     '735_800': []
    # }

    # for i in range(len(res_400_445)):
    #     if(res_captor_rayon[i] == 10):
    #         if(res_captor_hauteur[i] == 1000):
    #             res_exp_1_1000['400_445'].append(res_400_445[i])
    #             res_exp_1_1000['655_665'].append(res_655_665[i])
    #             res_exp_1_1000['735_800'].append(res_735_800[i])
    #         else:
    #             res_exp_1_1400['400_445'].append(res_400_445[i])
    #             res_exp_1_1400['655_665'].append(res_655_665[i])
    #             res_exp_1_1400['735_800'].append(res_735_800[i])


    # dir = "./res/"
    # for file in os.listdir(dir):
    #     if file.startswith("captor_result"):
    #         print(file)
    #         df = pd.read_csv(dir + file)
    #         m = re.findall(r"[^-]*", file)
    #         lw = m[4]
    #         hw = m[6]
    #         band = lw + "_" + hw

    #         for index, r in df.iterrows():
    #             if r["elevation"] == 1000:
    #                 cur_res_exp_1_1000[band].append(r["n_photons"])
    #             else:
    #                 cur_res_exp_1_1400[band].append(r["n_photons"])


    # x1_1000 = res_exp_1_1000['400_445']
    # x2_1000 = res_exp_1_1000['655_665']
    # x3_1000 = res_exp_1_1000['735_800']

    # x1_1400 = res_exp_1_1400['400_445']
    # x2_1400 = res_exp_1_1400['655_665']
    # x3_1400 = res_exp_1_1400['735_800']

    # y1_1000 = cur_res_exp_1_1000['400_445']
    # y2_1000 = cur_res_exp_1_1000['655_665']
    # y3_1000 = cur_res_exp_1_1000['735_800']

    # y1_1400 = cur_res_exp_1_1400['400_445']
    # y2_1400 = cur_res_exp_1_1400['655_665']
    # y3_1400 = cur_res_exp_1_1400['735_800']

    # #plot 400-445
    # fig1 = plt.figure(1)
    # x1 = np.concatenate((x1_1000, x1_1400))
    # y1 = np.concatenate((y1_1000, y1_1400))

    # plt.scatter(x1_1000, y1_1000, 20, 'b')
    # plt.scatter(x1_1400, y1_1400, 20, 'g')
    # plt.legend(["Captor height 1000", "Captor height 1400"])

    # z1 = np.polyfit(x1, y1, 1)
    # p1 = np.poly1d(z1)
    # plt.plot(x1, p1(x1), 'r')
    # plt.title("Wavelength 400-445 nm")
    # plt.xlabel("Results of SEC2")
    # plt.ylabel("Our results")
    # fig1.show()

    # #plot 655-665
    # fig2 = plt.figure(2)
    # x2 = np.concatenate((x2_1000, x2_1400))
    # y2 = np.concatenate((y2_1000, y2_1400))

    # plt.scatter(x2_1000, y2_1000, 20, 'b')
    # plt.scatter(x2_1400, y2_1400, 20, 'g')
    # plt.legend(["Captor height 1000", "Captor height 1400"])

    # z2 = np.polyfit(x2, y2, 1)
    # p2 = np.poly1d(z2)
    # plt.plot(x2, p2(x2), 'r')
    # plt.title("Wavelength 655-665 nm")
    # plt.xlabel("Results of SEC2")
    # plt.ylabel("Our results")
    # fig2.show()

    # #plot 735-800
    # fig3 = plt.figure(3)
    # x3 = np.concatenate((x3_1000, x3_1400))
    # y3 = np.concatenate((y3_1000, y3_1400))

    # plt.scatter(x3_1000, y3_1000, 20, 'b')
    # plt.scatter(x3_1400, y3_1400, 20, 'g')
    # plt.legend(["Captor height 1000", "Captor height 1400"])

    # z3 = np.polyfit(x3, y3, 1)
    # p3 = np.poly1d(z3)
    # plt.plot(x3, p3(x3), 'r')
    # plt.title("Wavelength 735-800 nm")
    # plt.xlabel("Results of SEC2")
    # plt.ylabel("Our results")
    # fig3.show()

    # input()
