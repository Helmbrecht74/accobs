

class acceptor:
    def __init__(self, srs, decider, observer):
        self.srs = srs
        self.decider = decider
        self.observer = observer
        
    def check_validity(self):
        return self.validity_obs_dec() and self.validity_srs_obs()
        
    
    def validity_obs_dec(self):
        return self.observer.output_alphabet() == self.decider.alphabet
    
    def validity_srs_obs(self):
        return self.srs.alphabet == self.observer.alphabet
        pass