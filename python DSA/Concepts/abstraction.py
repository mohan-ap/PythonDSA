from abc import ABC,abstractmethod

class AbsClass(ABC):
    def print(self):
        print("normal method from abstract class")
    @abstractmethod
    def task(self):
        print("abstract method")

class Class1(AbsClass):
     def task(self):
         print("class1 overridden method")
    
class Class2(AbsClass):
      def task(self):
           return super().task()
    

       
             

obj1=Class1()
obj1.print()
obj1.task()

obj2=Class2()
obj2.print()
obj2.task()