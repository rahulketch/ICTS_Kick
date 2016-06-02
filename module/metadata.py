
import numpy as np

class metadata:
	"""
	This class extracts the relevant metadata from the simulation's metadata.txt file. 
	The path has to be specified when initializing and object of this class
	"""
	def __init__(self,path):
		self.path = path
		self.getMeta()
	def getMeta(self):
		"""
		This method extracts the values of the relevant quantities and stores them to the corresponding variables
		"""
		meta = open(self.path+'metadata.txt','r')
		for line in meta:
			line = line.translate(None,",")
			line = line.split()
			if(len(line)<2):
				continue;
			var = line[0].translate(None," ")
			if var == 'initial-ADM-energy':
				self.initial_mass = float(line[2])
			if var == 'initial-ADM-linear-momentum':
				self.initial_p = np.array([float(line[2]),float(line[3]),float(line[4])])
			if var == 'initial-ADM-angular-momentum':
				self.initial_j = np.array([float(line[2]),float(line[3]),float(line[4])])
			if var == 'remnant-mass':
				self.remnant_mass = float(line[2])
			if var == 'remnant-spin':
				self.remnant_spin = np.array([float(line[2]),float(line[3]),float(line[4])])
			if var == 'initial-mass1':
				self.initial_mass1 = float(line[2])
			if var == 'initial-mass2':
				self.initial_mass2 = float(line[2])
			if var == 'initial-spin1':
				self.initial_spin1 = np.array([float(line[2]),float(line[3]),float(line[4])])
			if var == 'initial-spin2':
				self.initial_spin2 = np.array([float(line[2]),float(line[3]),float(line[4])])
			if var == 'alternative-names':
				self.alt_name = line[2]
			if var == 'simulation-name':
				self.simulation_name= line[2]
			if var == 'relaxed-measurement-time':
				self.relaxed_time= float(line[2]) 
