import numpy as np
from mpl_toolkits.basemap import Basemap
from netCDF4 import Dataset
import matplotlib.pyplot as plt
coef = np.loadtxt('coef.txt',delimiter=',')
info_2 = Dataset('lsmask.nc')
mask = info_2.variables['mask'][0,:,:].data
m = np.nonzero(coef)
a = np.shape(m)[1]

lon = np.shape(mask)[0]
lat = np.shape(mask)[1]
coef_g = np.zeros(a)
x = np.zeros(a)
y = np.zeros(a)
for i in range(a):
    coef_g[i] = coef[m[0][i]]
lat = np.mgrid[-89.5:90.5][::-1]
lon = np.mgrid[0.5:360.5]
alpha = np.shape(mask)[0]
beta = np.shape(mask)[1]
s = 0
n = 0
for i in range(alpha):
    for j in range(beta):
        if mask[i,j] == 1:
            if coef[s] != 0:
                x[n] = i
                y[n] = j
                n += 1
            s+=1
lat_g = np.zeros(a)
lon_g = np.zeros(a)
for i in range(a):
    lat_g[i] = lat[int(x[i])]
    lon_g[i] = lon[int(y[i])]
lon_max = 360.5
lat_max = 90.5

plt.figure(figsize=[10,10])
m = Basemap(llcrnrlon = 0, llcrnrlat = -90, urcrnrlon = 360, urcrnrlat = 90, ellps = 'WGS84')
plt.xlim(0, lon_max)
plt.ylim(-lat_max, lat_max)
sc = plt.scatter(lon_g, lat_g , marker = '.', c = coef_g, cmap = plt.get_cmap('seismic'), linewidths=5)
sc.set_clim(vmin=-0.08, vmax=0.08)
plt.colorbar()
plt.title('Coefficient')
m.drawcoastlines(linewidth=0.5)
plt.show()