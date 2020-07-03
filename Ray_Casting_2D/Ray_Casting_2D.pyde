from Boundary import *
from Particle import *
from Ray import *
import random
global walls
global ray
global particle
global xoff
global yoff
def setup():
    global walls
    global ray
    global particle
    global xoff
    global yoff
    xoff = 0
    yoff = 0
    size(1000, 800, P2D)
    walls = []
    for i in range(5):
        walls.append(Boundary(random.uniform(0, width), random.uniform(0, height), 
                              random.uniform(0, width), random.uniform(0, height)
                              ))
    ray = Ray(100, 200)
    particle = Particle()

def draw():
    global walls
    global ray
    global particle
    global xoff
    global yoff
    background(0)
    for wall in walls:
        wall.show()
    particle.update(noise(xoff)*width, noise(yoff)*height)
    particle.show()
    particle.look(walls)
    xoff += 0.01
    yoff += 0.01
