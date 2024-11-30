

class decider:
    def __init__(self, state_set, alphabet, transitions, final_states, initial_state):
        self.state_set = frozenset(state_set)
        self.alphabet = frozenset(alphabet)
        self.intial_state = initial_state
        self.transitions = transitions
        self.final_states = final_states
        
    def run_on_string(self, string):
        current_state = self.intial_state
        for symbol in string:
            current_state = self.transitions[current_state][symbol]
        return current_state in self.final_states