import numpy as np 

y_train = np.loadtxt('y_train.txt', delimiter=',')
y_test = np.loadtxt('y_test.txt', delimiter=',')

y_mean = np.average(y_train, axis=0)
y_test -= y_mean
y_train -= y_mean
np.savetxt('y_test.txt', y_test, delimiter=',')
np.savetxt('y_train.txt', y_train, delimiter=',')