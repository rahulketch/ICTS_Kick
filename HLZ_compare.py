import pickle
import numpy as np
import HLZ_recoil_fit as HLZ

#mpl.use('Agg')
import matplotlib.pyplot as plt
f=open('healy.dat','r')
itemlist = pickle.load(f)
f.close()
itemlist = np.array(itemlist)
name = itemlist[:,0]
q = [float(x) for x in itemlist[:,2]]
S1 = [float(x) for x in itemlist[:,3]]
S2 = [float(x) for x in itemlist[:,4]]
kick = [float(x) for x in itemlist[:,5]]
kick_error = [float(x) for x in itemlist[:,6]]
f = open('alignedSpinDeviation.csv','w')
f.write('Simulation,q,S1,S2,Kick Calculated (km/s),Estimated Error (km/s),Kick from Fit (km/s),Deviation(km/s)\n')
for i in range(len(q)):
	kick_fit = HLZ.bbh_recoil_HLZ_aligned(q[i],S1[i],S2[i])
	f.write('%s,%0.4f,%0.4f,%0.4f,%0.4f,%0.4f,%0.4f,%0.4f\n'%(name[i],q[i],S1[i],S2[i],kick[i],kick_error[i],kick_fit,kick[i]-kick_fit))
f.close()
