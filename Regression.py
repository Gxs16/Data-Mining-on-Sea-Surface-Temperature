import numpy as np
import sklearn.model_selection as sk_model_selection
from sklearn import linear_model
x = np.loadtxt('sst_ts.txt', delimiter=',')
y = np.loadtxt('BJ_week_ave.txt', delimiter=',')
y_std = np.std(y, axis = 0)
y /= y_std

reg = linear_model.LassoLars(alpha=0.001, max_iter=10000)
reg.fit(x, y)
y_fore = np.sum(x * reg.coef_, axis=1) + reg.intercept_
mae = np.average(abs(y_fore-y))
np.savetxt('y_fore.txt',y_fore, delimiter=',')
np.savetxt('coef.txt',reg.coef_, delimiter=',')
np.savetxt('mae.txt', mae)