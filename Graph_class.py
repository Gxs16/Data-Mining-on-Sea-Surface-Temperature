import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
clss = np.loadtxt('class30.txt',delimiter=',')
lat_max = 90.5
lat = np.mgrid[-90:91]
lon_max = 360.5
lon_min = -0.5
lon = np.mgrid[0:361]
clss = 30 - clss
plt.figure(figsize=[10,10])
m = Basemap(llcrnrlon = 0, llcrnrlat = -90, urcrnrlon = 360, urcrnrlat = 90, ellps = 'WGS84')
plt.xlim(0, lon_max)
plt.ylim(-lat_max, lat_max)
mesh = plt.pcolor(lon, -lat, clss, cmap=plt.get_cmap('terrain'))
#mesh.set_clim(vmin=-0.5, vmax=10.5)
plt.title('Class')
plt.colorbar()
m.drawcoastlines(linewidth=0.5)
plt.show()