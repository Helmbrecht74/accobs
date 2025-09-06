#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 13:53:33 2025

@author: peter
"""

class SRS_String:
    """
    A string for the SRS is just a normal string, but with a different order function.
    """
    def __init__(self, srs_string):
        self._srs_string = srs_string
        
    def __lt__(self, other): 
        """
        Configuration strings are ordered first by length 
        then by string order 
        """
        difference_in_length = len( other ) - len( self._srs_string ) 
        if difference_in_length > 0:
            return True
        elif (difference_in_length == 0 
              and self._srs_string < other.get_string() ):
            return True
        return False
    
    def __eq__(self, other): 
        """
        Para
        """
        return self._srs_string   == other.get_string() 
      
    def get_string(self): 
        """
        Para
        """
        return self._srs_string