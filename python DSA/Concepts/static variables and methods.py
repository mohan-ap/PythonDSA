class Member:
    course="JavaScript"            #class variable

    def __init__(self,name,age):   #instance variables
        self.name=name
        self.age=age
        #Member.course="python"   #we can change the value of static variable

    def getDetails(self):              #class method
        print(self.name , self.age, self.course)


    def add(a,b):                    #static method
        #print(name)                #we are not able to access non-static variable inside static method                    
        return a+b
    
m=Member("mohan",24)
print(m.name)
print(m.age)
print(m.getDetails())
#print(m.add(10,20))           TypeError: add() takes 2 positional arguments but 3 were given
#print(add(10,20))             NameError: nameve static method inside any class, we are only able to access the method with the help of class name 'add' is not defined, if you gi
print(Member.add(10,20))

print(m.course)                #we can access the static variable with the help of class name or object name
print(Member.course)

print(Member.course)
