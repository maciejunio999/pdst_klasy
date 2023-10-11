class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()
    
    @classmethod
    def num_of_people(cls):
        return cls.number_of_people
    
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person("Maciek")
p2 = Person("Lena")
p3 = Person("Ala")
print(Person.num_of_people())