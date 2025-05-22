

class decider:
    """
    Basically a deterministic finite automaton.
    """
    
    def __init__(self, state_set, alphabet, transitions, final_states, initial_state):
        self.state_set = frozenset(state_set)
        self.alphabet = frozenset(alphabet)
        self.intial_state = initial_state
        self.transitions = transitions
        self.final_states = final_states
        self.states_without_exit = set()
        
    def run_on_string(self, string):
        """
        Simulate the system's run on the string provided.
        """
        current_state = self.intial_state
        for symbol in string:
            current_state = self.transitions[current_state][symbol]
            print(" s: ", current_state)
        return current_state #in self.final_states
            
    def one_step(self, symbol, current_state):
        """
        Single step of the simulation
        """
        return self.transitions[current_state][symbol]

    def state_is_life(self, state):
        if state in self.states_without_exit:
            return False
        else:
            return True
    
    def set_state_without_exit(self, state):
        self.states_without_exit.add(state)
        
   
    def _find_states_without_exit(self):
        for state in self.state_set:
            
            self.states_without_exit.add(state)
