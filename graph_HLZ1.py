import pickle
import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D

#mpl.use('Agg')
import matplotlib.pyplot as plt
f=open('healy.dat','r')
itemlist = pickle.load(f)
itemlist = np.array(itemlist)
name = itemlist[:,0]
q = [float(x) for x in itemlist[:,2]]
S1 = [float(x) for x in itemlist[:,3]]
S2 = [float(x) for x in itemlist[:,4]]
kick = [float(x) for x in itemlist[:,5]]
kick_error = [float(x) for x in itemlist[:,6]]

print(1)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#for i in range(len(q)):
surf = ax.scatter(S1,S2, q, c=kick, marker='o')

ax.set_xlabel('S1')
ax.set_ylabel('S2')
ax.set_zlabel('q')
#ax.set_xlim(-1,1)
#ax.set_ylim(-1,1)

YY, XX = np.mgrid[-1:1.25:0.25, -1:1.25:0.25]

#ax.plot_wireframe(XX,YY,5, color = 'r')
#ax.plot_wireframe(XX,YY,2, color = 'g')
#ax.plot_wireframe(XX,YY,8, color = 'b')
fig.colorbar(surf, shrink=0.5, aspect=5)
# ax = fig.add_subplot(212, projection='3d')
# ax.view_init(30,0)
# surf = ax.scatter(S1,S2, q, c=kick, marker='o')
# plt.draw()


#for angle in range(0, 360):
    #ax.view_init(30, angle)
    #plt.draw()
plt.show()

