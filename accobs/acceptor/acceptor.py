

class acceptor:
    def __init__(self, srs, decider, observer):
        self.srs = srs
        self.decider = decider
        self.observer = observer
        
    
    def run_on_string(self, input_string):
        """
        Simulate the system's run on the string provided.
        """
        strings_already_processed = set()
        strings_not_yet_processed = { input_string }
        j = 0
        while bool( strings_not_yet_processed ):
            if j > 22: break
            j += 1
            current_string = strings_not_yet_processed.pop()
            strings_already_processed.add(current_string)
            print("Popped:   ", current_string)
            print(strings_not_yet_processed)
            for position in range( len( current_string ) ) :
                # print(current_string[:position] + '-e-'  + current_string[position+1:])
                new_string = current_string[:position] + 'e'  + current_string[position+1:]
                if new_string not in strings_already_processed: 
                    strings_not_yet_processed.add(new_string)
            print(strings_not_yet_processed)
            print(strings_already_processed)
            print("    --------------     ")
            
                
        
    
    def check_validity(self):
        """
        make sure all componnents have 
        corresponding interfaces (alphabets)
        """
        return self.validity_obs_dec() and self.validity_srs_obs()
        
    
    def validity_obs_dec(self):
        """
        Checks if the observer's output alphabet coincides with
        the decider's input alphabet.
        """
        return self.observer.output_alphabet() == self.decider.alphabet
    
    def validity_srs_obs(self):
        """
        Checks if the observer's input alphabet coincides with
        the string-rewriting system's alphabet.
        """
        return self.srs.alphabet == self.observer.alphabet
        pass