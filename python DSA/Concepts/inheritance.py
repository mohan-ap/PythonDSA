class person:
    def __init__(self,fname,lname):
        self.firstName=fname
        self.lastName=lname
    def printName(self):
        print(self.firstName,self.lastName)


class Student(person):    # if you don't want to define any properties or methods, use "pass" keyword
    pass

class Member(person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)  #or   person.__init__(self,fname,lname)

class Employee(Member):
    pass
         
class Guest(person):
    def __init__(self, fname, lname):       #adding property to the child class without additional arguments
        super().__init__(fname, lname)
        self.year=2023

class Master(person):
    def __init__(self, fname, lname,year):
        super().__init__(fname, lname)          #adding property to the child class by paasing the argument
        self.year=year

class Staff(person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)                 #adding methods to the child class
    def fullName(self):
        print("my first name is " ,self.firstName, " and lastname is ",self.lastName)

p=person("mohan","kumar")
print(p.firstName)
print(p.lastName)
p.printName()

s=Student("elan","cheliyan")
s.printName()

m=Member("siva","kumar")
m.printName()

e=Employee("harish","singh")
e.printName()

g=Guest("mohan","kumar")
print(g.year)

m=Master("mohan","kumar",1999)
print(m.year)

s=Staff("mohan","kumar")
s.fullName()
