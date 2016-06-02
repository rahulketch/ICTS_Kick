import numpy as np
import h5py
import metadata
import bisect
class Simulation:
	#The relaxed parameter decides if the calculations are to be done from the beginning or from the relaxed time
	def __init__(self,path,directory,relaxed = False):
		self.path = path
		self.directory = directory
		self.metadata = metadata.metadata(path)
		self.Evaluate(relaxed)
	def ALM(self,l,m):
		if m>l or m<-l or l<2 or l>8:
			return 0
		return self.alm[l-2][m+l]
	def Hcomp(self,l,m):
		if m>l or m<-l or l<2 or l>8:
			return 0
		return self.H2[l-2][m+l]
	#The relaxed parameter decides if the calculations are to be done from the beginning or from the relaxed time
   	def Evaluate(self,relaxed=False): 
   		input_file1 = h5py.File(self.path+'rhOverM_Asymptotic_GeometricUnits.h5','r')
   		self.alm = []
		self.H2 = []
		self.dt = 0
		self.time = 0


   		
		for l in range(2,9):
			self.alm.append([])
			self.H2.append([])
			for m in range(-l,l+1):
				SXS = input_file1[self.directory]['Y_l%i_m%i.dat'%(l,m)]
				H = SXS[:,1]+(0+1j)*SXS[:,2]
				t = SXS[:,0]
				#The following will slice the array depending on the Relaxed Time if the relaxed parameter is said to true
				if relaxed:
					i = bisect.bisect_right(t,self.metadata.relaxed_time)
					t = t[i:]
					H = H[i:]

				self.time = t
				self.dt = np.diff(t)
				Hdot = np.diff(H)/np.diff(t)
				self.alm[l-2].append(Hdot)
				self.H2[l-2].append(H[1:])


