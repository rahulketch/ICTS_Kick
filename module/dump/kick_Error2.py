import numpy as np 
import os
import remnant_quantities as rq
import simulation_data as sm
class Kick_Error():
	def __init__(self,path,directory):
		self.path = path
		self.directory = directory
		self.sortedResolution()
		self.getSimulation() 
		self.getKick()
	def sortedResolution(self):
		self.res = []
		for x in os.walk(self.path): #gets all the subdirectory names
			file = x[0][len(self.path)+1:]
			if file.startswith('Lev'): #checks if the subdirectory starts with 'Lev'
				self.res.append([file])
		for file in self.res:
			file.append(int(file[0][3:])) #extracts and appends the resolution number. For eg, 4 in case of Lev4
		self.res = sorted(self.res,key = lambda x : x[1]) #sorts the list on the resolution number.
	def getSimulation(self):
		new_path = self.path + '/' + self.res[-1][0] + '/'
		self.simulation = sm.Simulation(new_path,self.directory)
	def getKick(self):
		self.kick = rq.getKick(self.simulation)
	def highResKick(self):
		"""Returns the kick using the highest resolution available"""
		return self.kick


	def truncError(self):
		"""Compares the higest resolution with the next highest resolution to 
		find the difference and returns that value as the error"""
		
		if len(self.res)<2:
			return -1
		path2 = self.path + '/' + self.res[-2][0] + '/'
		sim2 =  sm.Simulation(path2,self.directory)
		kick2 = rq.getKick(sim2)
		error = np.abs(self.kick - kick2)
		return error

	# def extrapolationError(path,directory):
	# 	res = sortedResolution(path)
	# 	new_path = path + '/' + res[-1][0] + '/'
	# 	simulation1 = sm.Simulation(new_path,'Extrapolated_N2.dir')
	# 	simulation2 = sm.Simulation(new_path,'Extrapolated_N3.dir')
	# 	simulation3 = sm.Simulation(new_path,'Extrapolated_N4.dir')
	# 	simulation4 = sm.Simulation(new_path,'OutermostExtraction.dir')
	# 	kick1 = rq.getKick(simulation1)
	# 	kick2 = rq.getKick(simulation2)
	# 	kick3 = rq.getKick(simulation3)
	# 	kick4 = rq.getKick(simulation4)
	# 	kick = [kick1,kick2,kick3]
	# 	error = np.abs(max(kick)-min(kick))
	# 	return error
	def extrapolationError(self):
		new_path = self.path + '/' + self.res[-1][0] + '/'
		simulation1 = sm.Simulation(new_path,'Extrapolated_N2.dir')
		simulation2 = sm.Simulation(new_path,'Extrapolated_N3.dir')
		kick1 = rq.getKick(simulation1)
		kick2 = rq.getKick(simulation2)
		error = np.abs(kick1 - kick2)
		return error
	def limitedModesError(self):
		
		new_path = self.path + '/' + self.res[-1][0] + '/'
		simulation = sm.Simulation(new_path,self.directory)
		kick2 = rq.getKick(simulation,7)
		error = np.abs(self.kick - kick2)
		return error
	def junkError(self):
		new_path = self.path + '/' + self.res[-1][0] + '/'
		simulation2 = sm.Simulation(new_path,self.directory, relaxed = True)
		kick2 = rq.getKick(simulation2)
		error = np.abs(self.kick - kick2)
		return error

	def downSampleError(self):
		new_path = self.path + '/' + self.res[-1][0] + '/'
		simulation2 = sm.Simulation(new_path,self.directory, relaxed=False, downsample = 2 )
		kick2 = rq.getKick(simulation2)
		error = np.abs(self.kick-kick2)
		return error
	def getHighResSim(self):
		return self.simulation

