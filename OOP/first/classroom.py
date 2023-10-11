class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []
    
    def get_name(self):
         return self.name
    
    def get_age(self):
         return self.age
    
    def add_grade(self, grade):
        if type(grade) == type(1) and grade in range(1,7):
                self.grades.append(grade)
        else:
            print("Wrong type of grade")
    
    def get_grades(self):
        return self.grades 
    
    def get_avg_grade(self):
         o = 0
         for i in self.grades:
              o += i
         return o/len(self.grades)

class Course:
    def __init__(self, name, max_students):
          self.name = name
          self.max_students = max_students
          self.students = []
        
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
        else:
             print("Course is full")
    
    def get_students(self):
         return [(s.get_name(), s.get_age()) for s in self.students]
     

maciek = Student("Maciek", 23)
maciek.add_grade(4)
maciek.add_grade(6)
print(maciek.get_grades())
print(maciek.get_avg_grade())

course = Course("Math", 2)
course.add_student(maciek)

ala = Student("Ala", 23)
course.add_student(ala)

print(course.get_students())