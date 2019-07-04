from sklearn import linear_model
import numpy as np

sst_ts = np.loadtxt('sst_ts.txt', delimiter=',')
Precip = np.loadtxt('BJ_week_ave.txt', delimiter=',')

x_train = sst_ts[0:357, :]
y_train = Precip[0:357]
x_test = sst_ts[357:, :]
y_test = Precip[357:]

np.savetxt('x_train.txt', x_train, delimiter=',')
np.savetxt('y_train.txt', y_train, delimiter=',')
np.savetxt('x_test.txt', x_test, delimiter=',')
np.savetxt('y_test.txt', y_test, delimiter=',')