import numpy as np 
import os
import remnant_quantities as rq
import simulation_data as sm
class Error():
	def __init__(self,path,directory):
		self.path = path
		self.directory = directory
		self.sortedResolution()
		self.setSimulation() 
		#self.setKick()
		#self.setSpin()
		#self.setMass()
	
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

	def getHighResSim(self):
		return self.simulation
	def isMoreThanOneRes(self):
		"""Used to check if more than one resolution is available"""
		if len(self.res)<2:
			return False;
		return True;

	def setKick(self):
		self.kick = rq.getKick(self.simulation)
	def setSpin(self):
		self.spin = rq.getRemnantSpin(self.simulation)
	def setMass(self):
		self.mass = rq.getRemnantMass(self.simulation)


	def highResKick(self):
		"""Returns the kick using the highest resolution available"""
		return self.kick
	def highResSpin(self):
		"""Returns the remnant spin using the highest resolution available"""
		return self.spin
	def highResMass(self):
		"""Returns the remnant mass using the highest resolution available"""
		return self.mass

	def getSecondHighestResolution(self):
		"""Returns the simulation with the 2nd highest resolution. Used for calculating truncation error"""
		new_path = self.path + '/' + self.res[-2][0] + '/'
		return sm.Simulation(new_path,self.directory)	
	def getOutermostSimulation(self):
		"""Returns the outermost extraction of the simulation"""
		return sm.Simulation(self.new_path,'OutermostExtraction.dir')
	def getRelaxedTimeSimulation(self):
		"""Returns the simulation with relaxed time to get rid of junk radiation"""
		return sm.Simulation(self.new_path,self.directory,relaxed = False)
	def getDownsampledSimulation(self):
		"""Downsamples the data by 2 to estimate errors due to numerical routines"""
		return sm.Simulation(self.new_path,self.directory,downsample = 2)

	def truncErrorKick(self):
		"""Compares the higest resolution with the next highest resolution to 
		find the difference and returns that value as the error"""		
		if len(self.res)<2:
			return 0
		sim2 =  self.getSecondHighestResolution()
		kick2 = rq.getKick(sim2)
		error = np.abs(self.kick - kick2)
		return error

	def truncErrorSpin(self):
		"""Compares the higest resolution with the next highest resolution to 
		find the difference and returns that value as the error"""		
		if len(self.res)<2:
			return 0
		sim2 =  self.getSecondHighestResolution()
		spin2 = rq.getRemnantSpin(sim2)
		error = np.abs(self.spin - spin2)
		return error
	def truncErrorMass(self):
		"""Compares the higest resolution with the next highest resolution to 
		find the difference and returns that value as the error"""		
		if len(self.res)<2:
			return 0
		sim2 =  self.getSecondHighestResolution()
		mass2 = rq.getRemnantMass(sim2)
		error = np.abs(self.mass - mass2)
		return error

	def extrapolationErrorKick(self):
		simulation2 = self.getOutermostSimulation()
		kick2 = rq.getKick(simulation2)
		error = np.abs(self.kick - kick2)
		return error
	def extrapolationErrorSpin(self):
		simulation2 = self.getOutermostSimulation()
		spin2 = rq.getRemnantSpin(simulation2)
		error = np.abs(self.spin - spin2)
		return error
	def extrapolationErrorMass(self):
		simulation2 = self.getOutermostSimulation()
		mass2 = rq.getRemnantMass(simulation2)
		error = np.abs(self.mass - mass2)
		return error


	def limitedModesErrorKick(self):		
		kick2 = rq.getKick(self.simulation,7)
		error = np.abs(self.kick - kick2)
		return error
	def limitedModesErrorSpin(self):		
		spin2 = rq.getRemnantSpin(self.simulation,7)
		error = np.abs(self.spin - spin2)
		return error
	def limitedModesErrorMass(self):		
		mass2 = rq.getRemnantMass(self.simulation,7)
		error = np.abs(self.mass - mass2)
		return error

	def junkErrorKick(self):
		simulation2 = self.getRelaxedTimeSimulation()
		kick2 = rq.getKick(simulation2)
		error = np.abs(self.kick - kick2)
		return error
	def junkErrorSpin(self):
		simulation2 = self.getRelaxedTimeSimulation()
		spin2 = rq.getRemnantSpin(simulation2)
		error = np.abs(self.spin - spin2)
		return error
	def junkErrorMass(self):
		simulation2 = self.getRelaxedTimeSimulation()
		mass2 = rq.getRemnantMass(simulation2)
		error = np.abs(self.mass - mass2)
		return error


	def downSampleErrorKick(self):
		simulation2 = self.getDownsampledSimulation()
		kick2 = rq.getKick(simulation2)
		error = np.abs(self.kick-kick2)
		return error
	def downSampleErrorSpin(self):
		simulation2 = self.getDownsampledSimulation()
		spin2 = rq.getRemnantSpin(simulation2)
		error = np.abs(self.spin-spin2)
		return error
	def downSampleErrorMass(self):
		simulation2 = self.getDownsampledSimulation()
		mass2 = rq.getRemnantMass(simulation2)
		error = np.abs(self.mass-mass2)
		return error



	


