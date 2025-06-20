#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Provides a class for configuration of observer systems
"""

import SRS_string

class Obs_Sys_Configuration:
    """
    A configuration consists of the string on which the SRS works
    and of the observation thus far.
    """
    def __init__(self, srs_string, obs_string):
        self._srs_string = SRS_string(srs_string)
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
        Para
        """
        if (self._obs_string   == other.get_obs() 
              and self._srs_string.get_string() == other.get_srs_conf() ):
            return True
        return False
            
   
    def get_obs(self): 
        """
        Para
        """ 
        return self._obs_string
        
    def get_srs_conf(self): 
        """
        Para
        """  
        return self._srs_string.get_string()       