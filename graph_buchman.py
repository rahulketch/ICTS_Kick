import pickle
import numpy as np
import matplotlib
from mpldatacursor import datacursor
def kick_fit(n):
	A = 1.2e4
	B = -0.93

	kick = A*n*n*np.sqrt(1.0-4.*n)*(1+B*n)
	return kick 
import matplotlib.pyplot as plt
f=open('buchman.dat','r')
itemlist = pickle.load(f)
itemlist = np.array(itemlist)
name = itemlist[:,0]
eta = [float(x) for x in itemlist[:,1]]
kick = [float(x) for x in itemlist[:,2]]
kick_error = [float(x) for x in itemlist[:,3]]
n = np.arange(0.07999999999,0.2499999999999,0.001)
fit_kick = kick_fit(n)
print(itemlist)
plt.figure()
#plt.plot(itemlist[:,0],itemlist[:,1],marker = 'o',linestyle = 'None')
for i in range(len(eta)):
	plt.errorbar(eta[i],kick[i],yerr=kick_error[i], linestyle = 'None', marker = '.',color='b' )
plt.plot(n,fit_kick,label = 'Fit from Buchman et al',color='r')
plt.ylim(-1)
plt.xlabel('$\eta$')
plt.ylabel('Kick (km/s)')
plt.title('Non Spinning Kick')
plt.legend()
datacursor()
plt.savefig('buchman.jpg')

plt.show()
