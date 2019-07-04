import numpy as np 

#Transfer sst to data series
sst = np.loadtxt('std_sst.txt',delimiter=',')
span = 1
weeks = np.shape(sst)[0]
loc = np.shape(sst)[1]
sst_ts = np.zeros([weeks-span+1, loc*span])
for i in range(span):
    for j in range(loc):
        sst_ts[:, i*loc + j] = np.copy(sst[i:weeks-span+i+1, j])

np.savetxt('sst_ts.txt', sst_ts, delimiter=',')