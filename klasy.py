from math import fabs


class Shape:
    def __init__(self, a, b=None):
        self.a = a
        self.b = b

    def what_am_i(self):
        print("Jestem figurą!")


class Rectangle(Shape):
    def calculate_perimeter(self):
        return 2 * (self.a + self.b)

    def what_am_i(self):  # przykład przesłaniania metod
        print("Jestem prostokątem!")


class Square(Shape):
    def calculate_perimeter(self):
        return 4 * self.a

    def change_size(self, c):
        self.a = int(fabs(self.a - c))


sqr1 = Square(4)
print("Obwód pierwszego kwadratu to {}.".format(sqr1.calculate_perimeter()))
rect1 = Rectangle(3, 4)
print("Obwód pierwszego prostokąta to {}.".format(rect1.calculate_perimeter()))
sqr1.change_size(7)
print("Obwód pierwszego kwadratu po zmianie boku to {}.".format(sqr1.calculate_perimeter()))
sqr1.what_am_i()
rect1.what_am_i()
print("---------------------------------------------------------------------------------------------------------")


class Horse:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner


class Rider:
    def __init__(self, name):
        self.name = name


pan = Rider('Maciek')
kon = Horse('Kon', pan)
# odwołujemy sie do klasy Horse zeby dojsc kto jest
# wlascicielem a potem do klasy Rider zeby uzyskan info
# jakie jest jego imie, bez .name dostaniemy glupie gowno
# print(kon.owner) = <__main__.Rider object at 0x01ED9DD8>
print(kon.owner.name)
print(kon.name)
print("---------------------------------------------------------------------------------------------------------")


class Person:
    def __init__(self, name, age, sup=None):
        self.name = name
        self.age = age
        if 18 > self.age >= 0:
            self.sup = sup
        elif 18 < self.age:
            self.sup = "nobody"
        else:
            print("U dum")


person1 = Person("Joanna", 43)
person2 = Person("Alicja", 16, person1)
print("Imie pierwszej osoby to {}.".format(person1.name))
print("Wiek pierwszej osoby to {}.".format(person1.age))
print("Opiekunem pierwszej osoby jest {}.".format(person1.sup))
print("Imie drugiej osoby to {}.".format(person2.name))
print("Wiek drugiej osoby to {}.".format(person2.age))
print("Opiekunem drugiej osoby jest {}.".format(person2.sup.name))

