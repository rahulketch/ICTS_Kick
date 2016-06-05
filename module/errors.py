import numpy as np 
import os
import remnant_quantities as rq
import simulation_data as sm
class Kick_Error():
	def __init__(self,path,directory):
		self.path = path
		self.directory = directory
		self.sortedResolution()
		self.setSimulation() 
		self.setKick()
	
	def sortedResolution(self):
		"""Sorts the resolution orders. Used to extract the highest resolution dataset"""
		self.res = []
		for x in os.walk(self.path): #gets all the subdirectory names
			file = x[0][len(self.path)+1:]
			if file.startswith('Lev'): #checks if the subdirectory starts with 'Lev'
				self.res.append([file])
		for file in self.res:
			file.append(int(file[0][3:])) #extracts and appends the resolution number. For eg, 4 in case of Lev4
		self.res = sorted(self.res,key = lambda x : x[1]) #sorts the list on the resolution number.
	
	def setSimulation(self):
		"""Sets the simulation with the highest available resolution"""
		self.new_path = self.path + '/' + self.res[-1][0] + '/'
		self.simulation = sm.Simulation(self.new_path,self.directory)


	def setKick(self):
		self.kick = rq.getKick(self.simulation)


	def highResKick(self):
		"""Returns the kick using the highest resolution available"""
		return self.kick

	def getSecondHighestResolution(self):
		"""Returns the simulation with the 2nd highest resolution. Used for calculating truncation error"""
		new_path = self.path + '/' + self.res[-2][0] + '/'
		return sm.Simulation(new_path,self.directory)	
	def getOutermostSimulation(self):
		"""Returns the outermost extraction of the simulation"""
		return sm.Simulation(self.new_path,'OutermostExtraction.dir')
	def getRelaxedTimeSimulation(self):
		"""Returns the simulation with relaxed time to get rid of junk radiation"""
		return sm.Simulation(self.new_path,self.directory,relaxed = True)
	def getDownsampledSimulation(self):
		"""Downsamples the data by 2 to estimate errors due to numerical routines"""
		return sm.Simulation(self.new_path,self.directory,relaxed = False, downsample = 2)

	def truncErrorKick(self):
		"""Compares the higest resolution with the next highest resolution to 
		find the difference and returns that value as the error"""
		
		if len(self.res)<2:
			return -1
		sim2 =  self.getSecondHighestResolution()
		kick2 = rq.getKick(sim2)
		error = np.abs(self.kick - kick2)
		return error

	def extrapolationErrorKick(self):
		simulation2 = self.getOutermostSimulation()
		kick2 = rq.getKick(simulation2)
		error = np.abs(self.kick - kick2)
		return error
	def limitedModesErrorKick(self):		
		kick2 = rq.getKick(self.simulation,7)
		error = np.abs(self.kick - kick2)
		return error
	def junkErrorKick(self):
		simulation2 = self.getRelaxedTimeSimulation()
		kick2 = rq.getKick(simulation2)
		error = np.abs(self.kick - kick2)
		return error

	def downSampleErrorKick(self):

		simulation2 = self.getDownsampledSimulation()
		kick2 = rq.getKick(simulation2)
		error = np.abs(self.kick-kick2)
		return error
	
	def getHighResSim(self):
		return self.simulation

