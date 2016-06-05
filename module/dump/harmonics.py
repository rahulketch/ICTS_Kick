import numpy as np
import h5py
import metadata
class Simulation:
	def __init__(self,path,directory):
		self.path = path
		self.directory = directory
		self.metadata = metadata.metadata(path)
		self.Evaluate()
	def ALM(self,l,m):
		if m>l or m<-l or l<2 or l>8:
			return 0
		return self.alm[l-2][m+l]
	def Hcomp(self,l,m):
		if m>l or m<-l or l<2 or l>8:
			return 0
		return self.H2[l-2][m+l]
   	def Evaluate(self):
   		input_file1 = h5py.File(self.path+'rhOverM_Asymptotic_GeometricUnits.h5','r')
   		self.alm = []
		self.H2 = []
		self.time = 0
		self.dt = 0


   		
		for l in range(2,9):
			self.alm.append([])
			self.H2.append([])
			for m in range(-l,l+1):
				SXS = input_file1[self.directory]['Y_l%i_m%i.dat'%(l,m)]
				H = SXS[:,1]+(0+1j)*SXS[:,2]
				t = SXS[:,0]
				self.time = t
				self.dt = np.diff(t)
				Hdot = np.diff(H)/np.diff(t)
				self.alm[l-2].append(Hdot)
				self.H2[l-2].append(H[1:])

