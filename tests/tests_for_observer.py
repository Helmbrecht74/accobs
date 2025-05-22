#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 18:40:46 2024

@author: peter
"""

import sys
sys.path.insert(1, '..')
# make package accessible



from accobs.observer.observer import observer as obs 

states = { 'q1', 'q2' }
alph = { 'a', 'b' }
transitions = {
    'q1' : { 'a' : 'q1', 'b' : 'q2' },
    'q2' : { 'a' : 'q2', 'b' : 'q2' },
    }
outputf = { 'q1' : 'a', 'q2' : 'b' }

ob = obs( states, alph, transitions, outputf,  'q1' )


