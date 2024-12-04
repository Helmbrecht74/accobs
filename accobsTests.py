#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 18:40:46 2024

@author: peter
"""


from accobs.srs.srs import srs as SRS

#import accobs.srs.srs


rules = {  
    'a' : { 'bb' , 'c' },
    'b' : { 'cc' }
    }

rw = SRS( rules )

#rw = srs.srs( rules )
rw.set_start_string("abba")
print(rw.move_one())


#rw = srs.srs( rules )
rw.set_start_string("a")
print(rw.move_one())


from accobs.observer.observer import observer as obs 

states = { 'q1', 'q2' }
alph = { 'a', 'b' }
transitions = {
    'q1' : { 'a' : 'q1', 'b' : 'q2' },
    'q2' : { 'a' : 'q2', 'b' : 'q2' },
    }
outputf = { 'q1' : 'a', 'q2' : 'b' }

ob = obs( states, alph, transitions, outputf,  'q1' )

print(ob.run_on_string('aaaaa'))
print(ob.run_on_string('aababbaa'))
print("AusgAlph:  ", ob.output_alphabet())

from accobs.decider.decider import decider as deci 

states = { 'q1', 'q2' }
alph = { 'a', 'b' }
transitions = {
    'q1' : { 'a' : 'q1', 'b' : 'q2' },
    'q2' : { 'a' : 'q2', 'b' : 'q2' },
    }
outputf = { 'q1' : 'A', 'q2' : 'B' }

de = deci( states, alph, transitions, {'q2'}, 'q1')

print(de.run_on_string('aaaaa'))
print(de.run_on_string('aababbaa'))


from accobs.acceptor.acceptor import acceptor as acceptor

accs = acceptor(5, de, ob) 

print("Und " , accs.validity_obs_dec())
