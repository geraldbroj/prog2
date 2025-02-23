import math
import turtle

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

class Linea(Punto):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    def __str__(self):
        return f"Linea {self.p1},{self.p2}"
    def dibujaLinea(self):
        t = turtle.Turtle()
        
        t.penup()
        t.pensize(5)
        t.goto(p1.X, p1.Y)
        t.color("black")
        t.write(f"{self.p1} ", move=False, align="center", font=("Arial", 10, "normal"))
        t.color("red")
        t.pendown()
        t.goto(p2.X, p2.Y)
        t.color("black")
        t.write(f"{self.p2}", move=False, align="center", font=("Arial", 10, "normal"))
        turtle.done()


        
#        d = abs(self.p2.X - self.p1.Y)
 #       print(" ")
  #      for _ in range(d):
   #         print("-", end="")





class Circulo(Punto):
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio
    def __str__(self):
        return f"Circulo({self.centro},{self.radio})"
    def dibujaCirculo(self):
        c = turtle.Turtle()
        
        c.penup()
        c.pensize(3)
        c.goto(k.X, k.Y)
        c.pendown()
        c.circle(self.radio)


k = Punto(60,80)
r = Circulo(k,40)
print(r)
r.dibujaCirculo()
print("-----------------------------------------------")
p1 = Punto(3,5)
p2 = Punto(57,18)
l = Linea(p1, p2)
print(l)
l.dibujaLinea()
