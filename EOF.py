import numpy as np 
from sklearn.decomposition import PCA
from sklearn import linear_model
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from netCDF4 import Dataset



sst = np.loadtxt('std_sst.txt',delimiter=',')
info_2 = Dataset('lsmask.nc')
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
lon = np.shape(mask)[0]
lat = np.shape(mask)[1]
pca = PCA(n_components = 4)
pca.fit(sst)
EOF = pca.components_
new_EOF = np.zeros((4, lon, lat))
for i in range(4):
    s = 0
    for j in range(lon):
        for k in range(lat):
            if mask[j, k] == 1:
                new_EOF[i, j, k] = EOF[i, s]
                s += 1

lat_max = 90.5
lat = np.mgrid[-90:91]
lon_max = 360.5
lon_min = -0.5
lon = np.mgrid[0:361]
plt.figure(figsize=[10,10])
m = Basemap(llcrnrlon = 0, llcrnrlat = -90, urcrnrlon = 360, urcrnrlat = 90, ellps = 'WGS84')
plt.subplot(221)
plt.xlim(0, lon_max)
plt.ylim(-lat_max, lat_max)
mesh = plt.pcolor(lon, -lat, new_EOF[0,:,:], cmap=plt.get_cmap('coolwarm'))
mesh.set_clim(vmin=-0.018, vmax=0.018)
plt.title('EOF1')
plt.colorbar()
m.drawcoastlines(linewidth=0.5)

plt.subplot(222)
plt.xlim(0, lon_max)
plt.ylim(-lat_max, lat_max)
mesh = plt.pcolor(lon, -lat, new_EOF[1,:,:], cmap=plt.get_cmap('coolwarm'))
mesh.set_clim(vmin=-0.018, vmax=0.018)
plt.title('EOF2')
plt.colorbar()
m.drawcoastlines(linewidth=0.5)

plt.subplot(223)
plt.xlim(0, lon_max)
plt.ylim(-lat_max, lat_max)
mesh = plt.pcolor(lon, -lat, new_EOF[2,:,:], cmap=plt.get_cmap('coolwarm'))
mesh.set_clim(vmin=-0.018, vmax=0.018)
plt.title('EOF3')
plt.colorbar()
m.drawcoastlines(linewidth=0.5)

plt.subplot(224)
plt.xlim(0, lon_max)
plt.ylim(-lat_max, lat_max)
mesh = plt.pcolor(lon, -lat, new_EOF[3,:,:], cmap=plt.get_cmap('coolwarm'))
mesh.set_clim(vmin=-0.018, vmax=0.018)
plt.title('EOF4')
plt.colorbar()
m.drawcoastlines(linewidth=0.5)

plt.show()