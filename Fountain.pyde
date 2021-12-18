import sys

sys.path.append(".")
from particle import Particle
from system import ParticleSystem
from util import *

ps_list = []
def setup():
    size(640, 400)

    global ps
    ps = ParticleSystem(x0 = width / 2, y0 = height, yf = 0.75 * height)


def draw():
    background(0x1C1C1C)
    
    for ps in ps_list:
        ps.addParticle()
        ps.run()

def mousePressed():
    ps_list.append(ParticleSystem(x0 = mouseX, y0 = height, yf = mouseY))
        

    

    
    
