from util import *

class Particle:
    
    def __init__(self, x0, y0, vy_0 = -17.5, radius = 10):
        self.x0 = x0 + random(-1, 1)
        self.y0 = y0
        self.x = self.x0
        self.y = self.y0
        
        self.vx = random(-1, 1)
        
        self.vy_0 = vy_0
        self.vy = self.vy_0 + random(-2, 2)
        
        self.accy = 0.7
        self.accx = 0.01
        self.dt = 0.5
        
        self.radius = radius + int(random(-5, 5))

        colors = [color(0xF2727E), color(0xBEF272), color(0x72f2e6), color(0xa672f2)]
        index = int(random(len(colors)))
        self.alpha = 0xFF
    
        self.color = color(colors[index] + (self.alpha << 24))

                           
    def update(self):
        self.vx += (self.vx / abs(self.vx)) * self.accx * self.dt
        self.x += self.vx * self.dt
        
        self.vy += self.accy * self.dt
        self.y += self.vy * self.dt
    
        self.alpha *= exp(-.02 * self.dt)
        self.radius *= exp(-0.01 * self.dt)
    
    def display(self):
        noStroke()
        fill(self.color)
        ellipseMode(CENTER)
        ellipse(self.x, self.y, self.radius, self.radius)
        
    def reset(self):
        self.x = self.x0
        self.y = self.y0
        
        self.vx = random(-1, 1)
        self.vy = self.vy_0 + random(-2, 2)
        
        self.alpha = 255
        
    def outOfBounds(self):
        return self.x > width or self.x < 0 or self.y > height 
