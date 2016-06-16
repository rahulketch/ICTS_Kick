import pickle
import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

#mpl.use('Agg')
import matplotlib.pyplot as plt
f=open('healy.dat','r')
itemlist = pickle.load(f)
itemlist = np.array(itemlist)
name = itemlist[:,0]
q = [float(x) for x in itemlist[:,2]]
m1 = [float(x) for x in itemlist[:,3]]
m2 = [float(x) for x in itemlist[:,4]]
S1 = [float(x) for x in itemlist[:,5]]
S2 = [float(x) for x in itemlist[:,6]]
kick = [float(x) for x in itemlist[:,7]]
kick_error = [float(x) for x in itemlist[:,8]]


fig = plt.figure()
ax = Axes3D(fig)
#ax = fig.add_subplot(111, projection='3d')

def init():
	
	surf = ax.scatter(S1,S2, q, c=kick, marker='o')

	ax.set_xlabel('S1')
	ax.set_ylabel('S2')
	ax.set_zlabel('q')
	fig.colorbar(surf, shrink=0.5, aspect=5,label = 'Kick (km/s)')
def animate(i):
    ax.view_init(elev=20., azim=i)


anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=360, interval=5, blit=False)
#plt.show()
anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])


#for i in range(len(q)):

#ax.set_xlim(-1,1)
# #ax.set_ylim(-1,1)
# for ii in xrange(0,360,1):
#         ax.view_init(elev=10., azim=ii)
#         plt.savefig("movie"%ii+".png")

# YY, XX = np.mgrid[-1:1.25:0.25, -1:1.25:0.25]

#ax.plot_wireframe(XX,YY,5, color = 'r')
#ax.plot_wireframe(XX,YY,2, color = 'g')
#ax.plot_wireframe(XX,YY,8, color = 'b')

# ax = fig.add_subplot(212, projection='3d')
# ax.view_init(30,0)
# surf = ax.scatter(S1,S2, q, c=kick, marker='o')
# plt.draw()


#for angle in range(0, 360):
    #ax.view_init(30, angle)
    #plt.draw()
# plt.show()

