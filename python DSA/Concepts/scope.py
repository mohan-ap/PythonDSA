#Local scope 

def myfunc():
  x = 300
  print(x)        

myfunc()
#print(x)   name 'x' is not defined, not able to access outside the function

#function inside function

def myfun():
  x=100
  def innerfun():
    print(x)          #we can access the variable inside a inner function
  innerfun()
myfun()

#global scope

x=100
def myfun():
  print(x)        #we can access the global variable inside the function and outside the function
myfun()
print(x)

#same variable name 

x=100
def myfun():
  x=200
  print(x)  #200
myfun()
print(x)    #100

#global keyword

def myfun():
  global x
  x=200
myfun()
print(x)       #we make the "x variable as global scope with the help of global, now we can access it from anywhere"

