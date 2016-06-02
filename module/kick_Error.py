import numpy as np 
import os
import remnant_quantities as rq
import simulation_data as sm 
def sortedResolution(path):
	res = []
	for x in os.walk(path): #gets all the subdirectory names
		file = x[0][len(path)+1:]
		if file.startswith('Lev'): #checks if the subdirectory starts with 'Lev'
			res.append([file])
	for file in res:
		file.append(int(file[0][3:])) #extracts and appends the resolution number. For eg, 4 in case of Lev4
	res = sorted(res,key = lambda x : x[1]) #sorts the list on the resolution number.
	return res

def highResKick(path,directory):
	"""Returns the kick using the highest resolution available"""
	res = sortedResolution(path)
	new_path = path + '/' + res[-1][0] + '/'
	simulation = sm.Simulation(new_path,directory)
	return rq.getKick(simulation)


def truncError(path,directory):
	"""Compares the higest resolution with the next highest resolution to 
	find the difference and returns that value as the error"""
	res = sortedResolution(path)
	if len(res)<2:
		return -1
	path1 = path + '/' + res[-1][0] + '/'
	path2 = path + '/' + res[-2][0] + '/'
	sim1 =  sm.Simulation(path1,directory)
	sim2 =  sm.Simulation(path2,directory)
	kick1 = rq.getKick(sim1)
	kick2 = rq.getKick(sim2)
	error = np.abs(kick1 - kick2)
	return error

def extrapolationError(path,directory):
	res = sortedResolution(path)
	new_path = path + '/' + res[-1][0] + '/'
	simulation1 = sm.Simulation(new_path,'Extrapolated_N2.dir')
	simulation2 = sm.Simulation(new_path,'Extrapolated_N3.dir')
	simulation3 = sm.Simulation(new_path,'Extrapolated_N4.dir')
	simulation4 = sm.Simulation(new_path,'OutermostExtraction.dir')
	kick1 = rq.getKick(simulation1)
	kick2 = rq.getKick(simulation2)
	kick3 = rq.getKick(simulation3)
	kick4 = rq.getKick(simulation4)
	kick = [kick1,kick2,kick3]
	error = np.abs(max(kick)-min(kick))
	return error
def limitedModesError(path,directory):
	res = sortedResolution(path)
	new_path = path + '/' + res[-1][0] + '/'
	simulation = sm.Simulation(new_path,directory)
	kick1 = rq.getKick(simulation)
	kick2 = rq.getKick(simulation,7)
	error = np.abs(kick1 - kick2)
	return error

