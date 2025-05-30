#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 18:40:46 2024

@author: peter
"""


from accobs.srs.srs import srs as SRS

#import accobs.srs.srs


rules = {  
    'a' : { 'bb' , 'cc' },
    'b' : { 'cc' }
    }

rw = SRS( rules )



from accobs.observer.observer import observer as obs 

states = { 'q1', 'q2' }
alph = { 'a', 'b' }
transitions = {
    'q1' : { 'a' : 'q1', 'b' : 'q2' },
    'q2' : { 'a' : 'q2', 'b' : 'q2' },
    }
outputf = { 'q1' : 'a', 'q2' : 'b' }

ob = obs( states, alph, transitions, outputf,  'q1' )

# next

from accobs.decider.decider import decider as deci 

states = { 'q1', 'q2' }
alph = { 'a', 'b' }
transitions = {
    'q1' : { 'a' : 'q1', 'b' : 'q2' },
    'q2' : { 'a' : 'q2', 'b' : 'q2' },
    }
outputf = { 'q1' : 'A', 'q2' : 'B' }

de = deci( states, alph, transitions, {'q2'}, 'q1')


# other scenario

from accobs.acceptor.acceptor import acceptor as acceptor

rules = {  
    'a' : { 'bb' , 'c' },
    'b' : { 'cc' }
    }

rw = SRS( rules )

accs = acceptor(rw, de, ob) 
accs.run_on_string("aaa")
