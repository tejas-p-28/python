class University:
    def __init__(self):
        print("conductor of the base class")
        self.univ = "MIT"
    def display(self):
        print("the university name is:",{self.univ})
class Course(University):
    def __init__(self):
        print("Constructor of the child class 1of class university")
        University.__init__(self)
        self.course = "CSE"
    def display(self):
        print("the course name is:",{self.course})
        University.display(self)
class Branch(University):
    def __init__(self):
        print("Constructor of the child class 2 of class university")
        self.branch = "Data Science"
    def display(self):
        print("the branch name is:",{self.branch})
class Student(Course, Branch):
    def __init__(self):
        print("Constructor of child class of course and branch is called")
        self.name = "Tonny"
        Branch.__init__(self)
        Course.__init__(self)
    def display(self):
        print("the name of the student is:",{self.name})
        Branch.display(self)
        Course.display(self)
ob = Student()
print()
ob.display()