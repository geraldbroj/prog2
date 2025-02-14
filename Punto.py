import math

class Punto:
    def __init__(self, x , y):
        self.X = x
        self.Y = y
    def coord_cartesiana(self):
        return "Coordenadas {} {}".format(self.X, self.Y)
    def coord_polares(self):
        p1 = ((self.X)**2 + (self.Y)**2)**(1/2)
        p2 = math.degrees(math.atan2(self.Y, self.X))
        return "Coordenadas polares {} {:.2f}".format(p1,p2)
    def __str__(self):
        return f"Punto {self.X , self.Y}"


p = Punto(3, 4)
print(p.coord_cartesiana())
print(p.coord_polares())
print(p)