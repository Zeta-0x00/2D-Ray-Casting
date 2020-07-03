class Ray:
    def __init__(self, ps, angle):
        self.pos = ps
        self.dir = PVector.fromAngle(angle)
    def show(self):
        stroke(255)
        push()
        translate(self.pos.x, self.pos.y)
        line(0, 0, self.dir.x * 10, self.dir.y * 10)
        pop()
    def lookAt(self, x, y):
        self.dir.x = x - self.pos.x
        self.dir.y = y - self.pos.y
        self.dir.normalize()
    def cast(self, wall):
        x1 = wall.a.x
        y1 = wall.a.y
        x2 = wall.b.x
        y2 = wall.b.y
        
        x3 = self.pos.x
        y3 = self.pos.y
        x4 = self.pos.x + self.dir.x
        y4 = self.pos.y + self.dir.y
        
        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if (den == 0):
            print('0')
            return
        t = ( (x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4) ) / den
        u = - ( (x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3) ) / den
        if (t > 0 and t < 1 and u > 0):
            pt = PVector()
            pt.x = x1 + t * (x2 - x1)
            pt.y = y1 + t * (y2 - y1)
            return pt
        else:
            return
