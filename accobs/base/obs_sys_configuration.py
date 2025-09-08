#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Provides a class for configuration of observer systems.
The configuration consists of the string of observations up to the current
point and the current string of the SRS.
The class facilitates comparison via == and < where the order is
   1. by the length of the observation / computation
   2. by the SRS string
Note that < and > can both result in False, while == also results in False,
if the observations are of equal lengths but different, while the SRS strings 
are the same.
  
The class facilitates access to the SRS string via indexing
"""

import base.SRS_string

class Obs_Sys_Configuration:
    """
    A configuration consists of the string on which the SRS works
    and of the observation thus far.
    """
    def __init__(self, srs_string, obs_string):
        self._srs_string = base.SRS_string.SRS_String(srs_string)
        self._obs_string = obs_string
        
    def __lt__(self, other): 
        """
        Configurations are ordered first by the length of the computation thus far,
        then by first length then string order on the SRS part
        """
        difference_in_length = len( other.get_obs() ) - len( self.get_obs() ) 
        if difference_in_length > 0:
            return True
        elif (difference_in_length == 0 
              and self._srs_string.get_string() < other.get_srs_conf() ):
            return True
        return False
    
    def __eq__(self, other): 
        """
        Equality check on both components
        """
        if (self._obs_string   == other.get_obs() 
              and self._srs_string.get_string() == other.get_srs_conf() ):
            return True
        return False
    
    def __getitem__(self, index):
        """
        Equality check on both components
        """
        return self._obs_string[index]
    
    def __str__(self):
        """
        Formatting to string
        """
        return ("SRS: " + self._obs_string 
                + ";  observation: " + self._srs_string.get_string())
            
   
    def get_obs(self): 
        """
        Getter for observation
        """ 
        return self._obs_string
        
    def get_srs_conf(self): 
        """
        Getter for SRS string
        """  
        return self._srs_string.get_string()       