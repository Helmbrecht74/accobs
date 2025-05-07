#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Provides the queue that manages the order in which the simulation
of an observer system is done
"""

import configuration

class ConfigQueue:
    """
    ddd
    """
    def __init__(self):
        self._queue = []
        
    def insert(self, new_configuration):
        """
        Parameters
        ----------
        configuration : a Configuration instance

        Returns
        -------
        None.

        """
        for element in self._queue:
            pass
            