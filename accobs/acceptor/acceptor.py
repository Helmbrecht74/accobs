

class acceptor:
    def __init__(self, srs, decider, observer):
        self.srs = srs
        self.decider = decider
        self.observer = observer
        
    def check_validity(self):
        self.validity_obs_dec()
        pass
    
    def validity_obs_dec(self):
        return self.observer.output_alphabet() == self.decider.alphabet
    
    def validity_srs_obs(self):
        # checks whether alphabet of SRS is input of observer
        pass