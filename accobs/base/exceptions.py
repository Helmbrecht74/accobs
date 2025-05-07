#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Provides a class for configuration of observer systems
"""

class AccobsError(Exception):
    """
    Base class for error from accobs package.
    """
    pass


class StateFormatError(AccobsError):
    """
    Base class for error from accobs package.
    """
    pass


class ConfigStringError(AccobsError):
    """
    Base class for error from accobs package.
    """
    pass
