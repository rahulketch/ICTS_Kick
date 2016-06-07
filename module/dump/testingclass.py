#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import h5py
import test.metadata as meta
import harmonics
speed_of_light = 299792.458

path = '../../Data/011/Lev5/' #path for the simulation
extrapolation_order = 2
savefig = False
A  = harmonics.harmonics(path,'Extrapolated_N%i.dir'%(extrapolation_order))




def norm(vector):
    return np.sqrt(vector[0]*vector[0]+vector[1]*vector[1]+vector[2]*vector[2])

metadata = meta.metadata(path)