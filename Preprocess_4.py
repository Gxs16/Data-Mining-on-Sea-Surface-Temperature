import numpy as np 
from netCDF4 import Dataset
sst = np.loadtxt('new_SST.txt',delimiter=',')
info_2 = Dataset('lsmask.nc')#Read Land Mask file
mask = info_2.variables['mask'][0,:,:].data

sst_wk_mean = np.zeros([52,int(np.sum(mask))])
wk_s = np.arange(0,364,52)#training 7 years 364 weeks
for i in range(52):
    sst_wk_mean[i] = np.copy(np.average(sst[i: :52, :], axis=0))
for i in range(52):
    sst[i: :52, :] -= sst_wk_mean[i]#all data minus the historical average sst
sst_std = np.std(sst[0:364, :], axis = 0)
sst /= sst_std
np.savetxt('std_sst.txt', sst, delimiter=',')