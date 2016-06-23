import numpy as np
import os
import errors
import simulation_data as sd
import remnant_quantities as rq
import pickle
main_path = '../data/simulations/'
directory = 'Extrapolated_N2.dir'
data = []
data = os.walk(main_path).next()[1]


f = open('all_kick_2.dat','w')
kicks = []
countdown = len(data)

for file in data:
    print("Started: " + file)
    path = main_path + file
    err = errors.Error(path,directory)
    err.setKick()
    err.setMass()
    err.setSpin()
    err.setErrors()
    err.deleteSimulation()
    kicks.append(err)
    print('Done! ' + ' Left:%d'%(countdown))
    countdown = countdown-1
pickle.dump(kicks,f)
f.close()