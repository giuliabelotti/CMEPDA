import math 

class Particle:
    """La classe rappresenta una generica particella"""
    def __init__(self, mass, charge, name, momentum = 0.):
    
#solo momentum è opzionale e lo inizializzo a zero

        self._mass = mass
        self._charge = charge
        self._name = name
        self.momentum = momentum 
        
    def info(self): 
        """ Stampo a video informazioni sulla prticella""" 
        message = 'Particle "{}": mass = {:.3f} MeV/c^2, charge = {} e '\
                  'momentum = {:.3f} MeV/c'
        print(message.format(self.name, self.mass, self.charge, self.momentum))
        
      
    @property
    def mass(self):
        return self._mass
        
    @property
    def charge(self):
        return self._charge
        
    @property
    def name(self):
        return self._name
    
    @property
    def momentum(self):
        return self._momentum
        
    @momentum.setter    
    def momentum(self, value):
        if value < 0:
            print('La particella ha impulso negativo!')
            print('L\'impulso sara\'settato a zero.')
            self._momentum = 0
        else:
            self._momentum = value
            
    @property 
    def energy(self):
        return math.sqrt(self.mass**2 + self.momentum**2)
        
    @energy.setter
    def energy(self, value):
        if value < self.mass: 
            print('La particella ha energia minore della sua massa!')
        else:
            self.momentum = math.sqrt(self.energy**2 - self.mass**2)
            
class Protons(Particle):
    def __init__(self, momentum = 0.):
        Particle.__init__(self, 938, +1, 'Protone', momentum) 
 
class Alpha(Particle):
    def __init__(self, momentum = 0.):
        Particle.__init__(self, 3727, +4, 'Alpha', momentum)        
    

if __name__ == '__main__':
    
    proton = Protons(200.)
    proton.energy = 1000.
    proton.info()
    
    alpha = Alpha(20.)
    alpha.energy = 10000.
    alpha.info()


    
