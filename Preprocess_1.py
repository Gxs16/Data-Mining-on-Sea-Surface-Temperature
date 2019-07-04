import numpy as np

info_1 = Dataset('sst.wkmean.1990-present.nc')#Read SST file
info_2 = Dataset('lsmask.nc')#Read Land Mask file, 

SST = info_1.variables['sst'][:,:,:].data#Extract SST data
mask = info_2.variables['mask'][0,:,:].data#Extract lands mask data

SST_total = np.zeros((len(SST),int(mask.sum())))
s = 0
for i in range(180):
    for j in range(360):
        if mask[i, j] == 1:
            SST_total[:, s] += SST[:, i, j]
            s += 1  # Reshape SST from 3D into 2D
 
#index 2009-1-4~2018-12-29, 521 weeks total
#1989-12-31~2009-1-3 992weeks total
new_SST = SST_total[991:1512,:]
np.savetxt('new_SST.txt', new_SST, delimiter = ',')
np.savetxt('mask.txt', mask, delimiter = ',')