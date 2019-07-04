import numpy as np 
from sklearn.decomposition import PCA
from sklearn import linear_model
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from sklearn.cluster import KMeans

sst = np.loadtxt('delinear_sst.txt',delimiter=',')
info_2 = Dataset('lsmask.nc')
mask = info_2.variables['mask'][0,:,:].data

pca = PCA(n_components = 100)
pca.fit(sst)
new_sst = pca.fit_transform(sst)

kmeans = KMeans(n_clusters=30).fit(sst.T)

lon = np.shape(mask)[0]
lat = np.shape(mask)[1]
clss = np.zeros((lon, lat))
s = 0
color = kmeans.labels_
color += 1
for j in range(lon):
    for k in range(lat):
        if mask[j, k] == 1:
            clss[j, k] = color[s]
            s += 1
np.savetxt('class30.txt', clss, delimiter=',')
'''lat_max = 90.5
lat = np.mgrid[-90:91]
lon_max = 360.5
lon_min = -0.5
lon = np.mgrid[0:361]
plt.figure(figsize=[10,10])
m = Basemap(llcrnrlon = 0, llcrnrlat = -90, urcrnrlon = 360, urcrnrlat = 90, ellps = 'WGS84')
plt.xlim(0, lon_max)
plt.ylim(-lat_max, lat_max)
mesh = plt.pcolor(lon, -lat, clss, cmap=plt.get_cmap('Set3'))
#mesh.set_clim(vmin=0, vmax=10)
plt.title('Class')
plt.colorbar()
m.drawcoastlines(linewidth=0.5)
plt.show()'''