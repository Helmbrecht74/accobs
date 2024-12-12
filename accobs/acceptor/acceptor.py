

class acceptor:
    def __init__(self, srs, decider, observer):
        self.srs = srs
        self.decider = decider
        self.observer = observer
        
    
    def run_on_string(self, input_string):
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
        return self.validity_obs_dec() and self.validity_srs_obs()
        
    
    def validity_obs_dec(self):
        return self.observer.output_alphabet() == self.decider.alphabet
    
    def validity_srs_obs(self):
        return self.srs.alphabet == self.observer.alphabet
        pass