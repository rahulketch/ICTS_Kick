import pickle
import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import HLZ_recoil_fit as HLZ

#mpl.use('Agg')
import matplotlib.pyplot as plt
f=open('healy.dat','r')
itemlist = pickle.load(f)
itemlist = np.array(itemlist)
name = itemlist[:,0]
q = np.array([float(x) for x in itemlist[:,2]])
m1 = np.array([float(x) for x in itemlist[:,3]])
m2 = np.array([float(x) for x in itemlist[:,4]])
S1 = (np.array([float(x) for x in itemlist[:,5]]))
S2 = (np.array([float(x) for x in itemlist[:,6]]))
kick = np.array([float(x) for x in itemlist[:,7]])
kick_error = np.array([float(x) for x in itemlist[:,8]])
eta = q/((1+q)**2)
delta  = (S2/m2 - S1/m1)/(m1+m2)
kick_fit = np.array([])
for i in range(len(q)):
	kick_fit = np.append(kick_fit,HLZ.bbh_recoil_HLZ_aligned(q[i],S1[i]/(m1[i]**2),S2[i]/(m2[i]**2)))
kick_deviation_fit = kick - kick_fit

err = np.array([])
KICK = np.array([])
ETA = np.array([])
DELTA = np.array([])
for i in range(len(q)):
	if kick_error[i] < np.abs(kick_deviation_fit[i]) or True:
		#	if kick_deviation_fit[i]<0:
			#err = np.append(err , kick_deviation_fit[i] + kick_error[i])
		#else:
			#err = np.append(err,kick_deviation_fit[i] - kick_error[i])
		err = np.append(err,kick_deviation_fit[i])
		KICK = np.append(KICK,kick[i])
		ETA = np.append(ETA,eta[i])
		DELTA = np.append(DELTA,delta[i])

plt.figure(1)
surf = plt.scatter(ETA,err,c = KICK, marker = 'o')
plt.xlabel(r'$\eta$')
plt.ylabel('Residue after error (km/s)')
plt.title('Residue from HLZ fit after estimated error substracted')
plt.colorbar(surf, shrink=0.5, aspect=5,label = 'Calculated Kick (km/s)')
plt.savefig('HLZ_eta.jpg')
#plt.plot(eta,kick_deviation_fit,line)
plt.show()
plt.figure(2)
surf = plt.scatter(DELTA,err,c = KICK, marker = 'o')
plt.xlabel(r'$\Delta$')
plt.ylabel('Residue after error (km/s)')
plt.title('Residue from HLZ fit after estimated error substracted')
plt.colorbar(surf, shrink=0.5, aspect=5,label = 'Calculated Kick (km/s)')
plt.savefig('HLZ_delta.jpg')
#plt.plot(eta,kick_deviation_fit,line)
plt.show()