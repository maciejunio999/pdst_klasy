# import matplotlib.patches as pt
from turtle import *
import math
import numpy


class Prostokat:

    def __init__(self, a, b):
        self.dlugosc = a * 10
        self.szerokosc = b * 10
        print("prostokąt")


    def pole(self):
        return self.dlugosc * self.szerokosc


    def rysowanie(self, zulw):
        self.x = self.dlugosc / (-2)
        self.y = self.szerokosc / 2
        self.z = zulw
        self.z.penup()
        self.msg = "Prostokąt"
        self.z.goto(0, self.szerokosc)
        self.z.color("black")
        self.z.pendown()
        self.z.write(self.msg, move=False, align="center", font=("Arial", 15, "bold"))
        self.z.color("white")
        self.z.goto(self.x, self.y)
        self.z.color("black")
        self.z.fillcolor('black')
        self.z.begin_fill()
        for i in range(2):
            self.z.forward(self.dlugosc)
            self.z.right(90)
            self.z.forward(self.szerokosc)
            self.z.right(90)
        self.z.end_fill()
        self.z.hideturtle()
        self.z.getscreen()._root.mainloop()


class Circle:

    def __init__(self, r):
        self.promien = r * 10
        print("Koło")


    def pole(self):
        return math.pi * self.promien * self.promien


    def rysowanie(self, zulw):
        self.z = zulw
        self.z.penup()
        self.msg = "Koło"
        self.h = self.promien + 40
        self.z.goto(0, self.h)
        self.z.color("black")
        self.z.pendown()
        self.z.write(self.msg, move=False, align="center", font=("Arial", 15, "bold"))
        self.z.penup()
        self.z.color('black')
        self.z.fillcolor('black')
        self.z.goto(0, 0)
        self.z.pendown()
        self.z.begin_fill()
        self.z.circle(self.promien)
        self.z.end_fill()
        self.z.hideturtle()
        self.z.getscreen()._root.mainloop()


class Triangle:

    def __init__(self, bok1, bok2, bok3):
        self.a = bok1
        self.b = bok2
        self.c = bok3
        self.p = (bok1 + bok2 + bok3) / 2
        print("Trójkąt")


    def pole(self):
        return math.sqrt(self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))


    def rysowanie(self, zulw):
        self.z = zulw
        self.z.penup()
        self.msg = "Trójkąt"
        self.h = self.c ** 2 - ((self.c ** 2 + self.a ** 2 - self.b ** 2) / (2 * self.a)) ** 2
        self.z.goto(0, (self.h + 40))
        self.z.color("black")
        self.z.pendown()
        self.z.write(self.msg, move=False, align="center", font=("Arial", 15, "bold"))
        self.alfa = round(((numpy.arcsin(self.h / self.b) * 180) / math.pi), 2)
        self.gamma = round(((numpy.arcsin(self.h / self.c) * 180) / math.pi), 2)
        self.beta = 180 - self.alfa - self.gamma
        self.kat = 270 - (0.5 * self.gamma)
        self.r = round((math.sqrt(((self.p - self.a) * (self.p - self.b) * (self.p - self.c)) / self.p)), 2)
        self.R = round(((self.a * self.b * self.c) / (4 * self.r * self.p)), 2)
        self.z.penup()
        self.z.color('white')
        self.z.goto(0, 0)
        self.z.right(self.kat)
        self.z.forward(self.R)
        self.z.right(0)
        self.z.color('black')
        self.z.fillcolor('black')
        self.z.begin_fill()
        self.z.pendown()
        self.z.forward(self.a)
        self.z.right(180 - self.alfa)
        self.z.forward(self.b)
        self.z.right(2 * self.gamma + self.alfa + self.beta)
        self.z.forward(self.c)
        self.z.end_fill()
        self.z.hideturtle()
        self.z.getscreen()._root.mainloop()


zolwik = Turtle()
zolwik.speed(2)
screen = zolwik.getscreen()
screen.bgcolor('white')
screen.title("Karteczka")
screen.setup(width=0.5, height=0.5)


prostokat1 = Prostokat(2, 3)
print(prostokat1.pole())
prostokat1.rysowanie(zolwik)


kolo1 = Circle(4)
print(kolo1.pole())
# kolo1.rysowanie(zolwik)


trojkat1 = Triangle(3, 4, 5)
print(trojkat1.pole())
# trojkat1.rysowanie(zolwik)
