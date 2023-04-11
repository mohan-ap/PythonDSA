class DuckTyping():
    def  add(self,a,b):    #polymorphism
        return a+b

dt=DuckTyping()
print(dt.add(10,20))
print(dt.add([10,20,30],[40,50,60]))
print(dt.add("mohan","kumar"))