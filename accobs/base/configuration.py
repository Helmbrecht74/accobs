#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Provides a class for configuration of observer systems
"""

class Configuration:
    """
    dddbc
    """
    def __init__(self, srs_string, obs_string):
        self._srs_string = srs_string
        self._obs_string = obs_string
        
    def __lt__(self, other): 
        """
        Para
        """
        difference_in_length = len( other.get_obs() ) - len( self._obs_string ) 
        if difference_in_length > 0:
            return True
        elif (difference_in_length == 0 
              and self._srs_string < other.get_srs_conf() ):
            return True
        return False
    
    def __eq__(self, other): 
        """
        Para
        """
        if (self._obs_string   == other.get_obs() 
              and self._srs_string == other.get_srs_conf() ):
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
        return self._srs_string           