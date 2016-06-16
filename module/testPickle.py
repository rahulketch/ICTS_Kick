import metadata 
import Kick_pickle
import numpy as np
import pickle
f = open('data5.dat','r')
list = pickle.load(f)
for entry in list:
	print(entry.metadata.alt_name,entry.kick,entry.Max_Error,entry.Max_Error_Source)
f.close()