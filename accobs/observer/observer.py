

class observer:
    def __init__(self, state_set, alphabet, transitions, output, initial_state):
        self.state_set = frozenset(state_set)
        self.alphabet = frozenset(alphabet)
        self.intial_state = initial_state
        self.output = output
        self.transitions = transitions
        
    def run_on_string(self, string):
        current_state = self.intial_state
        for symbol in string:
            current_state = self.transitions[current_state][symbol]
        return self.output[current_state]
    
    def output_alphabet(self):
        return frozenset(self.output.values())