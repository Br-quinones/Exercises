# The exercise requires building a class hierarchy where a parent class, SchoolMember, defines basic attributes like name and age. You then create two subclasses, Student and Teacher, which use the super() function to inherit those shared attributes while adding their own specific details, such as grades or subjects.

class SchoolMember():
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

class Student(SchoolMember):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def study(self):
        print(f"Hello, I am {self.name}, I am {self.age} years old and I am in grade {self.grade}")

class Teacher(SchoolMember):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching {self.subject}")
