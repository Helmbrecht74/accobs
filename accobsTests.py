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