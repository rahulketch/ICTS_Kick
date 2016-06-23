import numpy as np 
import os
import remnant_quantities as rq
import simulation_data as sm
import metadata
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
		self.metadata = self.simulation.metadata

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

	def setTruncErrorKick(self):
		"""Compares the higest resolution with the next highest resolution to 
		find the difference and returns that value as the error"""		
		if len(self.res)<2:
			self.truncErrorKick = 0.0
			return
		sim2 =  self.getSecondHighestResolution()
		kick2 = rq.getKick(sim2)
		error = np.abs(self.kick - kick2)
		self.truncErrorKick = error

	def setTruncErrorSpin(self):
		"""Compares the higest resolution with the next highest resolution to 
		find the difference and returns that value as the error"""		
		if len(self.res)<2:
			self.truncErrorSpin = 0.0
			return
		sim2 =  self.getSecondHighestResolution()
		spin2 = rq.getRemnantSpin(sim2)
		error = np.abs(self.spin - spin2)
		self.truncErrorSpin = error
	def setTruncErrorMass(self):
		"""Compares the higest resolution with the next highest resolution to 
		find the difference and returns that value as the error"""		
		if len(self.res)<2:
			self.truncErrorMass = 0.0
			return
		sim2 =  self.getSecondHighestResolution()
		mass2 = rq.getRemnantMass(sim2)
		error = np.abs(self.mass - mass2)
		self.truncErrorMass = error

	def setExtrapolationErrorKick(self):
		"""Compares with the OutermostKick"""
		simulation2 = self.getOutermostSimulation()
		kick2 = rq.getKick(simulation2)
		error = np.abs(self.kick - kick2)
		self.extrapolationErrorKick = error
	def setExtrapolationErrorSpin(self):
		"""Compares with the OutermostKick"""
		simulation2 = self.getOutermostSimulation()
		spin2 = rq.getRemnantSpin(simulation2)
		error = np.abs(self.spin - spin2)
		self.extrapolationErrorSpin = error
	def setExtrapolationErrorMass(self):
		"""Compares with the OutermostKick"""
		simulation2 = self.getOutermostSimulation()
		mass2 = rq.getRemnantMass(simulation2)
		error = np.abs(self.mass - mass2)
		self.extrapolationErrorMass = error


	def setLimitedModesErrorKick(self):	
		"""Takes Ylm modes till l = 7 and compares with l=8"""	
		kick2 = rq.getKick(self.simulation,7)
		error = np.abs(self.kick - kick2)
		self.limitedModesErrorKick = error
	def setLimitedModesErrorSpin(self):
		"""Takes Ylm modes till l = 7 and compares with l=8"""			
		spin2 = rq.getRemnantSpin(self.simulation,7)
		error = np.abs(self.spin - spin2)
		self.limitedModesErrorSpin = error
	def setLimitedModesErrorMass(self):
		"""Takes Ylm modes till l = 7 and compares with l=8"""			
		mass2 = rq.getRemnantMass(self.simulation,7)
		error = np.abs(self.mass - mass2)
		self.limitedModesErrorMass = error

	def setJunkErrorKick(self):
		"""Finds the value by doing the integration before the relaxed time as well 
			and quotes the difference"""
		simulation2 = self.getRelaxedTimeSimulation()
		kick2 = rq.getKick(simulation2)
		error = np.abs(self.kick - kick2)
		self.junkErrorKick = error
	def setJunkErrorSpin(self):
		"""Finds the value by doing the integration before the relaxed time as well 
			and quotes the difference"""
		simulation2 = self.getRelaxedTimeSimulation()
		spin2 = rq.getRemnantSpin(simulation2)
		error = np.abs(self.spin - spin2)
		self.junkErrorSpin = error
	def setJunkErrorMass(self):
		"""Finds the value by doing the integration before the relaxed time as well 
			and quotes the difference"""
		simulation2 = self.getRelaxedTimeSimulation()
		mass2 = rq.getRemnantMass(simulation2)
		error = np.abs(self.mass - mass2)
		self.junkErrorMass = error


	def setDownSampleErrorKick(self):
		"""Divides the time resolution by a factor of 2 and compares the result"""
		simulation2 = self.getDownsampledSimulation()
		kick2 = rq.getKick(simulation2)
		error = np.abs(self.kick-kick2)
		self.downSampleErrorKick = error
	def setDownSampleErrorSpin(self):
		"""Divides the time resolution by a factor of 2 and compares the result"""
		simulation2 = self.getDownsampledSimulation()
		spin2 = rq.getRemnantSpin(simulation2)
		error = np.abs(self.spin-spin2)
		self.downSampleErrorSpin = error
	def setDownSampleErrorMass(self):
		"""Divides the time resolution by a factor of 2 and compares the result"""
		simulation2 = self.getDownsampledSimulation()
		mass2 = rq.getRemnantMass(simulation2)
		error = np.abs(self.mass-mass2)
		self.downSampleErrorMass = error
	
	def setTotalErrorKick(self):
		"""Adds the errors in quadrature"""
		self.totalErrorKick = rq.errorQuadrature(np.array([self.truncErrorKick,self.extrapolationErrorKick,self.limitedModesErrorKick,
			self.junkErrorKick,self.downSampleErrorKick]))
	def setTotalErrorSpin(self):
		"""Adds the errors in quadrature"""
		self.totalErrorSpin = rq.errorQuadrature([self.truncErrorSpin,self.extrapolationErrorSpin,self.limitedModesErrorSpin,
			self.junkErrorSpin,self.downSampleErrorSpin])
	def setTotalErrorMass(self):
		"""Adds the errors in quadrature"""
		self.totalErrorMass = rq.errorQuadrature([self.truncErrorMass,self.extrapolationErrorMass,self.limitedModesErrorMass,
			self.junkErrorMass,self.downSampleErrorMass])

	def setKickErrors(self):
		self.setTruncErrorKick()
		self.setExtrapolationErrorKick()
		self.setLimitedModesErrorKick()
		self.setJunkErrorKick()
		self.setDownSampleErrorKick()
		self.setTotalErrorKick()
	
	def setSpinErrors(self):
		self.setTruncErrorSpin()
		self.setExtrapolationErrorSpin()
		self.setLimitedModesErrorSpin()
		self.setJunkErrorSpin()
		self.setDownSampleErrorSpin()
		self.setTotalErrorSpin()

	def setMassErrors(self):
		self.setTruncErrorMass()
		self.setExtrapolationErrorMass()
		self.setLimitedModesErrorMass()
		self.setJunkErrorMass()
		self.setDownSampleErrorMass()
		self.setTotalErrorMass()

	def setErrors(self):
		self.setKickErrors()
		self.setSpinErrors()
		self.setMassErrors()

	def deleteSimulation(self):
		"""This is just to be able to store a variable of this class without taking too much memory"""
		self.simulation = None
	


