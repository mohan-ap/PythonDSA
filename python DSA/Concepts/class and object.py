class demo:
    #Name="mohan"  # have to initilize values
    #age=26
    def __init__(self,name,age):   #used to initalize value to object variables, it is like constructors
        self.name=name             #Instead of self we can use other names but it should be first argument
        self.age=age
    
    def __str__(self):
        return f"{self.name} {self.age}"


    '''def __init__(self,name,age,place):
        self.name=name
        self.age=age                      #multiple init method not possible
        self.place=place'''
    
    
    def details(self):
        print("my name is {} and age is {}".format(self.name,self.age))

p1=demo("mohan",24)
print(p1.name)     #to access the property value of an object
print(p1.age)   
p1.details()
p2=demo("elan",26)
print(p2.name)
print(p2.age)
p2.details()

print(p1)          #<__main__.demo object at 0x7fda8e809040> in-bulit __str__() returns. we can override this method

p1.age=25          #to change the property value of an object
print(p1.age)   

del p1.age        #to delete the property of an object
#print(p1.age)     #output: AttributeError: 'demo' object has no attribute 'age'

del p1           #to delete an object
#print(p1)        #AttributeError: 'demo' object has no attribute 'age'




