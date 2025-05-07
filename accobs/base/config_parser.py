#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Provides a class for configuration of observer systems
"""



import re
from exceptions import ConfigStringError


class ConfigurationParser(Exception):
    """
    Base class for error from accobs package.
    """
    @staticmethod
    def parse_string( string_to_parse ):
        parsed_list = re.findall("[a-zA-Z]\d*", string_to_parse)
        if string_to_parse != "".join( parsed_list ):
            raise ConfigStringError("The string does not represent a configuration.")
        return parsed_list
    
s="abq1q22e33rtz4r"
s="ab.q1q22e33rtz4r"

print(ConfigurationParser.parse_string(s))

