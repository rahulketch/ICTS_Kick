import numpy as np
import os
import errors
import simulation_data as sd
import remnant_quantities as rq


class spreadsheet_entry():
    def __init__(self,path,directory):
        self.path = path
        self.directory = directory
        self.setQuantitites()
    def setQuantitites(self):
        
        err = errors.Error(self.path,self.directory)        
        sim = err.getHighResSim()        
        self.metadata = sim.metadata
        self.isMoreThanOneRes = err.isMoreThanOneRes()
        
        err.setKick()


        

        V_trunc = err.truncErrorKick()
        V_mode = err.limitedModesErrorKick()
        V_extrap = err.extrapolationErrorKick()
        V_junk = err.junkErrorKick()
        V_downsample = err.downSampleErrorKick()
    
        kick_error = [[V_trunc,'Truncation'],[V_mode,'Limited Modes'],
                      [V_extrap,'Extrapolation'],[V_junk,'Junk Radiation']
                      ,[V_downsample,'Downsampling']]
              

        kick_error = sorted(kick_error)

        self.total_kick_error = rq.errorQuadrature(kick_error)
        self.V_trunc = V_trunc
        self.V_mode = V_mode
        self.V_extrap = V_extrap
        self.V_downsample = V_downsample    
        self.V_junk = V_junk
        self.Max_Error = kick_error[-1][0]
        self.Max_Error_Source = kick_error[-1][1]
        self.kick = err.highResKick()


