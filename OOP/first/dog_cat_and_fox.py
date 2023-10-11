from main import Animal

class Dog(Animal):
    def speak(self):
        print('bark')
    
    def get_name(self):
        return "You have a right to remain silent, i am " + self.name

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def speak(self):
        print('meow')

    def get_color(self):
        return self.color

class Fox(Animal):
    pass

d = Dog("Tofik")
print(d.get_name())
d.speak()

c = Cat("Kotek", "red")
print(c.get_name())
print(c.get_color())
c.speak()

f = Fox("Foxy")
print(f.get_name())
f.speak()