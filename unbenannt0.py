#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 09:43:48 2025

@author: peter
"""


class C :
    def mein_dict(self):
        self.x = 55
        lokal = self.__dict__
        klasse = C.__dict__
        return lokal | klasse
        
c = C()
print(type(c.mein_dict()))