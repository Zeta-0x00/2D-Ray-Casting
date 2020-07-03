from Boundary import *
from Ray import *

class Particle:
    def __init__(self):
        self.pos = PVector(width / 2, height / 2)
        self.rays = []
        for i in range(0, 360, 1):
            self.rays.append( Ray(self.pos, radians(i) ) )
    def show(self):
        fill(255)
        ellipse(self.pos.x, self.pos.y, 16, 0.0)
        for i in range(0, len(self.rays)):
            self.rays[i].show()          
    def look(self,walls):
       closest = None
       for ray in self.rays:
           for wall in walls:
               record = float('inf')
               pt = ray.cast(wall)
               if(pt):
                d = PVector.dist(self.pos, pt)
                if(d < record):
                    closest = pt
           if (closest):
               line(self.pos.x, self.pos.y, closest.x, closest.y)                     
    def update(self, x, y):
        self.pos.set(x, y)
