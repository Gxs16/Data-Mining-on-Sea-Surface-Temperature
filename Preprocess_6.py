import numpy as np 
from sklearn.decomposition import PCA
from sklearn import linear_model
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from sklearn.cluster import KMeans


sst = np.loadtxt('std_sst.txt',delimiter=',')
info_2 = Dataset('lsmask.nc')#Read Land Mask file
mask = info_2.variables['mask'][0,:,:].data
x = np.arange(521)
y = np.array([np.average(row) for row in sst])

reg = linear_model.LinearRegression()

for i in range(int(np.sum(mask))):
    y = sst[:, i]
    reg.fit(np.array([x]).T, y)
    y = x * reg.coef_ +reg.intercept_
    sst[:,i] -= y

b = np.mean(sst, axis=0)
sst -= b
np.savetxt('delinear_sst.txt', sst, delimiter=',')