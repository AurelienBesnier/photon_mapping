import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re


if __name__ == "__main__":
    
    xls = pd.ExcelFile(r"simuMesureExpes12_tout.xls") # use r before absolute file path 

    res_simulation = xls.parse(0) #2 is the sheet number+1 thus if the file has only 1 sheet write 0 in paranthesis
    
    res_600_655 = res_simulation['600_655_mumolM2S_mes']
    res_655_665 = res_simulation['655_665_mumolM2S_mes']
    
    xSite = [610,710,110,110,1210,1210,110,110,1210,1210,610,610]
    ySite = [1330,1330,930,930,930,930,1330,1330,1330,1330,1130,1130]
    zSite = [1400,1400,1400,1000,1400,1000,1400,1000,1400,1000,1400,1000]
    
    for i in range(len(res_600_655)):
    	for j in range(12):
    	   if int(res_simulation['xSite'][i]) == xSite[j] and int(res_simulation['ySite'][i]) == ySite[j] and int(res_simulation['zSite'][i]) == zSite[j]:
    	   	print(res_simulation['xSite'][i],res_simulation['ySite'][i],res_simulation['zSite'][i],res_600_655[i])
   
      
    
    
