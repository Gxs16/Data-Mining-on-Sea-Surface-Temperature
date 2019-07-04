from netCDF4 import Dataset
import numpy as np
import os
folder = 'Precip'
files = os.listdir(folder)

info = Dataset(folder+'\\precip.2009.nc')
precip_BJ = np.zeros([3652,1])
m = 0
for file in files:
    info = Dataset(folder+'\\'+file)
    precip = info.variables['precip'][:,:,:].data 
    for i in range(np.shape(precip)[0]):
        havedata = 0
        sum = 0
        for lat in range(9):
            for lon in range(21):
                if precip[i, lat+97, lon+225] >= 0:
                    sum += precip[i, lat+97, lon+225]
                    havedata +=1
        precip_BJ[i+m] = sum / havedata * 189
    m = m + np.shape(precip)[0]
np.savetxt('BJ.txt', precip_BJ, delimiter=',')
#Huabei Area 37.25N-41.25N, 112.75E,122.75E, lat[97,106] lon[225,246]