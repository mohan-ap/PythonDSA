#without private 
class Member():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def details(self):
        print("my name is {} and age is {}".format(self.name,self.age))

m=Member("mohan",24)
m.details()
print(m.age)
print(m.name)

m.name="kumar"
m.age=25
m.details()
print(m.age)
print(m.name)

#with private data member
class Member():
    pin=5678
    def __init__(self,name,age):                #in python to make private use double underscores
        self.__name=name
        self.__age=age
    
    def setDetails(self,name,age,pin):           #setter method
        if self.pin==pin:
            self.__name=name
            self.__age=age
        else:
            print("wrong pin, Access not permitted")
            exit()
 
    def getDetails(self):                        #getters method
         print("my name is {} and age is {}".format(self.__name,self.__age))

m=Member("mohan",24)
m.getDetails()
#print(m.__name)           #'Member' object has no attribute '__name'
#print(m.__age)            #'Member' object has no attribute '__age'
m.__name="kumar"             #does not gives error but value not change, to change the value use set methds
m.__age=25
m.getDetails()             #my name is mohan and age is 24
m.setDetails("kumar",25,5678)
m.getDetails()


#Mangling

class Member():
    def __init__(self,name,age):                
        self.__name=name
        self.__age=age

    def getDetails(self,name,age):
       print("my name is {} and age is {}".format(self.__name,self.__age))

m=Member("mohan",24)
print(m._Member__name)     #mangling --- with the help of class name we can access private data outside the class, so in python private is not efficient
m._Member__name="kumar"
print(m._Member__name)  

