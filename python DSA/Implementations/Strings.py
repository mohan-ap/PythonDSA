s1="mohan"
s2='kumar'
s3='''ap'''
s4="""123"""

print(s1+" "+s2+" "+s3+" "+s4)

s="Hello world"
print('hello')
print("world")
print()


#multiline strings
a="""mohan 
kumar
ap"""                   #for multiline strings have to use three double quotes or three single quotes

#or

a='''mohan
kumar
ap'''

print("\"multiline string\"")
print(a)
print()


#string are arrays
a="hello world"
print(a[1])      
print()

#looping a string

for x in "hello world":
    print(x)
print()

#to find length of a string
a="hello"
print("length of string")
print(len(a))
print()

#string slicing
a="mohan kumar"       # to print range of characters
print(a[0:3])
print(a[:4])
print(a[2:])
print(a[-4:-2])

#Modify String
s="hello world"
x=s.capitalize()  # first character cap
print(x)

x=s.lower()
print(x)      #returns all characters in lower case

x=s.upper()   # returns all characters in upper case
print(x)

x=s.split(" ")  #returns string of array
print(x)

x=s.title()    # returns each words first character in cap
print(x)

x=s.replace("world","python")
print(x)

#string concatenation 
s1="mohan"
s2="kumar"
s3=s1+s2
print(s3)
#or
s3=s1+" "+s2
print(s3)

#format strings
age=24
text="my name is mohan and my age is {}"  #one argument
print(text.format(age))

place="erode"
text="my name is mohan, age {} and i am from {}"  #multiple arguments
print(text.format(age,place))

name="mohan"
text="my name is {1}, age {0} and i am from {2}"   #using indexes
print(text.format(age,name,place))


