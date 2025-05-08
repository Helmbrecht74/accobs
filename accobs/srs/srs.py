#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class srs:
    """
    Provides methods to simulate a string-rewriting system.
    The rule set is passed to the constructor in the form
    of a dictionary, where the keys are the left-hand sides
    of the rewrite rules; the right-hand sides are represented
    by sets of strings, which contain all possible right-hand
    sides for the given left-hand side.
    """
  
    def __init__( self, rule_set, alphabet = set() ):
        self.rule_set = rule_set
        if alphabet == set():
            alphabet = set( rule_set.keys() )
        self.current_string = ""

    def set_start_string( self, start_string ):
        """
        Sets the start string for simulations.
        """
        self.current_string = start_string
        
    def move_one( self, start_string = None ):
        if start_string == None:
            base_string = self.current_string
        else:
            base_string = start_string
            
        resulting_strings = set()
        for position in range( len( base_string ) ):
            for left_hand_side, right_hand_sides in self.rule_set.items():
                if base_string[position] == left_hand_side:
                    for right_hand_side in right_hand_sides:
                        resulting_strings.add( base_string[:position] + right_hand_side 
                                              + base_string[position+1:] )
        return resulting_strings
    
    
    def terminating_symbols(self):
        # works only for painter and CF systems
        return self.alphabet - self.srs.rule_set.keys()
    
    def is_painter( self ):
        """
        Tests if the rule set contains only painter rules.
        """
        if ( max( map(len, self.rule_set.keys() )) == 1
                and max( map(len, self.rule_set.values() )) == 1 
                ):
            return True
        return False
    
    
    def is_cf( self ):
        """
        Tests if the rule set contains only context-free rules.
        """
        if ( max( map(len, self.rule_set.keys() )) == 1
                and min( map(len, self.rule_set.values() )) == 1 
                ):
            return True
        return False