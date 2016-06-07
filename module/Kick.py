
# coding: utf-8

# In[5]:

import numpy as np
import os
import errors
import simulation_data as sd
import remnant_quantities as rq
main_path = '../../Data/'
directory = 'Extrapolated_N2.dir'
data = []
data = os.walk(main_path).next()[1]
err = errors.Error('../../Data/011',directory)


# In[6]:

f = open('data4.csv','w')
f.write('Name,Alt_name,q,S1x,S1y,S1z,S2x,S2y,S2z,relaxed_eccentricity,no_of_orbits,')
f.write('Remnant_spin_hor,Calculated_Spin,Deviation_from_Horizon,Error_Estimate,Max_Error(Magnitutde),Max_Error_Source,')
f.write('Remnant_Mass_Hor,Remnant_Mass_Calc,Deviation_from_Horizon,Error_Estimate,Max_Error,')
f.write('Max_Error_Source,Kick(km/s),Total_Error(km/s),Max_Error,Max_Error_Source,')
f.write('V_mode(km/s),V_trunc(km/s),V_extrap(km/s),V_junk(km/s),V_downsample(km/s)\n')
for file in data:
    path = main_path + file
    err = errors.Error(path,directory)
    sim = err.getHighResSim()
    Name = sim.metadata.simulation_name
    Alt_name_list = sim.metadata.alt_name
    for name in Alt_name_list:
        if name.startswith('SXS'):
            Alt_name = name
    q = sim.metadata.initial_mass1/sim.metadata.initial_mass2
    S1 = sim.metadata.relaxed_spin1/(sim.metadata.relaxed_mass1**2)
    S2 = sim.metadata.relaxed_spin2/(sim.metadata.relaxed_mass2**2)
    
    Remnant_spin_hor = rq.norm(sim.metadata.remnant_spin)/(sim.metadata.remnant_mass**2)
    
    S1x = S1[0]
    S1y = S1[1]
    S1z = S1[2]
    S2x = S2[0]
    S2y = S2[1]
    S2z = S2[2]
    relaxed_eccentricity = sim.metadata.relaxed_eccentricity
    no_of_orbits = sim.metadata.no_of_orbits
    Calculated_Spin = rq.norm(rq.getRemnantSpinComponents(sim))/(sim.metadata.remnant_mass**2)
    More_than_one_res = err.isMoreThanOneRes()
    
    deviation_spin = rq.deviation(Remnant_spin_hor,Calculated_Spin)
    
    
    f.write('%s,%s,%0.3f,%0.4f,%0.4f,%0.4f,%0.4f,%0.4f,%0.4f,%s,%0.4f,'%(Name,Alt_name,q,S1x,S1y,S1z,S2x,S2y,S2z,
                                                                            relaxed_eccentricity,no_of_orbits))
    
    
    spin_error = [[err.truncErrorSpin(),'Truncation'],[err.limitedModesErrorSpin(),'Limited Modes'],
                  [err.extrapolationErrorSpin(),'Extrapolation'],[err.junkErrorSpin(),'Junk Radiation']
                  ,[err.downSampleErrorSpin(),'Downsampling']]
    total_spin_error = rq.errorQuadrature(spin_error)/(sim.metadata.remnant_mass ** 2)
    
    mass_error = [[err.truncErrorMass(),'Truncation'],[err.limitedModesErrorMass(),'Limited Modes'],
                  [err.extrapolationErrorMass(),'Extrapolation'],[err.junkErrorMass(),'Junk Radiation']
                  ,[err.downSampleErrorMass(),'Downsampling']]
    total_mass_error = rq.errorQuadrature(mass_error)
    
    kick_error = [[err.truncErrorKick(),'Truncation'],[err.limitedModesErrorKick(),'Limited Modes'],
                  [err.extrapolationErrorKick(),'Extrapolation'],[err.junkErrorKick(),'Junk Radiation']
                  ,[err.downSampleErrorKick(),'Downsampling']]
    total_kick_error = rq.errorQuadrature(kick_error)
    
    spin_error = sorted(spin_error)
    mass_error = sorted(mass_error)
    kick_error = sorted(kick_error)
    if(More_than_one_res):
        f.write('%0.4f,%0.4f,%0.4f,%0.4f,%0.4f,%s,'%(Remnant_spin_hor,Calculated_Spin,deviation_spin,total_spin_error,
                                                     spin_error[-1][0]/(sim.metadata.remnant_mass**2),spin_error[-1][1]))
    else:
        f.write('%0.4f,%0.4f,%0.4f,%0.4f*,%0.4f,%s,'%(Remnant_spin_hor,Calculated_Spin,deviation_spin,total_spin_error,
                                                     spin_error[-1][0]/(sim.metadata.remnant_mass**2),spin_error[-1][1]))
        
    Remnant_Mass_Hor = sim.metadata.remnant_mass
    Remnant_Mass_Calc = err.highResMass()
    deviation_mass = rq.deviation(Remnant_Mass_Hor,Remnant_Mass_Calc)
    
    Max_Error_mass = mass_error[-1][0]
    Max_Error_Source_mass = mass_error[-1][1]
    if(More_than_one_res):
        f.write('%0.4f,%0.4f,%0.4f,%0.4f,%0.4f,%s,'%(Remnant_Mass_Hor,Remnant_Mass_Calc,deviation_spin,total_mass_error,
                                                     Max_Error_mass,Max_Error_Source_mass))
    else:
        f.write('%0.4f,%0.4f,%0.4f,%0.4f*,%0.4f,%s,'%(Remnant_Mass_Hor,Remnant_Mass_Calc,deviation_mass,total_mass_error,
                                                     Max_Error_mass,Max_Error_Source_mass))
    
    Kick = err.highResKick()
    V_trunc = err.truncErrorKick()
    V_mode = err.limitedModesErrorKick()
    V_extrap = err.extrapolationErrorKick()
    V_junk = err.junkErrorKick()
    V_downsample = err.downSampleErrorKick()
    if(More_than_one_res):
        f.write('%f,%f,%f,%s,'%(Kick,total_kick_error,kick_error[-1][0],kick_error[-1][1]))
        f.write('%f,%f,%f,%f,%f'%(V_mode,V_trunc,V_extrap,V_junk,V_downsample))
    else:
        f.write('%f,%f*,%f,%s,'%(Kick,total_kick_error,kick_error[-1][0],kick_error[-1][1]))
        f.write('%f,-,%f,%f,%f'%(V_mode,V_extrap,V_junk,V_downsample))
    f.write('\n')
    print('Done: '+Alt_name)
f.close()
    


# In[ ]:




# In[3]:




# In[ ]:



