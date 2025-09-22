

from accobs.base import exceptions, obs_sys_configuration 

class acceptor:
    def __init__(self, srs, decider, observer):
        self.srs = srs
        self.decider = decider
        self.observer = observer
        
        if not self.validity_obs_dec():
            raise exceptions.AlphabetsIncompatibleError("Observer output alphabet not equal to decider input alphabet.")
        
        if not self.validity_srs_obs():
            raise exceptions.AlphabetsIncompatibleError("SRS alphabet not equal to observer input alphabet.")
        
    
    def run_on_string(self, input_string, max_steps = 1000):
        """
        Simulate the system's run on the string provided.
        The maximal depth of the computation (number of steps) is max_steps.
        Because of the width of the computation tree, many more steps overall
        can be computed.
        """
        initial_config = obs_sys_configuration ( input_string, "" )
        configs_already_processed = set()
        configs_not_yet_processed = { initial_config }

        while bool( configs_not_yet_processed ):

            current_config = configs_not_yet_processed.pop()
            configs_already_processed.add(current_config)
            print("Popped:   ", current_config)
            print(configs_not_yet_processed)
            for new_string in self.srs.move_one(current_config.get_srs_conf()):
                new_observation = current_config.get_obs() + self.observer.run_on_string(new_string)
                new_config = obs_sys_configuration ( new_string, new_observation )
                if new_config not in configs_already_processed: 
                    configs_not_yet_processed.add(new_config)
            print(configs_not_yet_processed)
            print(configs_already_processed)
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