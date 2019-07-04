import numpy as np 

precip = np.loadtxt('BJ.txt')
precip_time = precip[3:3650]
precip_week_mean = np.empty(521)
for week in range(521):
        precip_week_mean[week] = np.sum(precip_time[(7*week):(7*week+7)]) / 7
np.savetxt('BJ_week_ave.txt', precip_week_mean, delimiter=',')