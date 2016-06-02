import numpy as np 
import os
import remnant_quantities as rq
import simulation_data as sm 
def highResKick(path,directory):
	res = []
	for x in os.walk(path): #gets all the subdirectory names
		file = x[0][len(path)+1:]
		if file.startswith('Lev'): #checks if the subdirectory starts with 'Lev'
			res.append([file])
		for file in res:
			file.append(int(file[0][3:])) #extracts and appends the resolution number. For eg, 4 in case of Lev4
		res = sorted(res,key = lambda x : x[1]) #sorts the list on the resolution number.
		new_path = path + '/' + res[-1][0]
		simulation = sm.Simulation(new_path,directory)
		return rq.getKick(simulation)
		
	