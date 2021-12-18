from particle import Particle
from util import *

class ParticleSystem:
    
    def __init__(self, x0, y0, yf):
        self.x0 = x0
        self.y0 = y0
        
        # yf = 0.5 * acc * t^2 + v0 * t + y0
        # v0 + acc * t = 0
        # ------------------
        # v0 = sqrt(2 * (y0 - yf) * acc)
        self.v0 = - sqrt(2 * (y0 - yf) * GRAVITY)
        self.particles = []
        
        for p in range(50):
            self.addParticle()
            
    def addParticle(self):
        self.particles.append( Particle(x0 = self.x0, y0 = self.y0, vy_0 = self.v0) )
        
    def run(self):
        
        for i, p in enumerate(self.particles):
            p.display()
            p.update()
            if p.outOfBounds():
                to_delete = self.particles.pop(i)
                del to_delete    # not sure if there's a more elegant way to keep mem small
        
