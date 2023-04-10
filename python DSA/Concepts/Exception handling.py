#raise an exception
'''def main():
    x=int(input("enter a value of x "))
    if(x>5):
        raise Exception ("x should not exceed 5.The value of x was:{}".format(x))
main()'''

#Asert an exception
'''import sys
assert ('Linux' in sys.platform), "This code is only runs in linux platform"'''

#eg:2
# x=int(input("enter a value of x "))
# if(x<5):
#     print("ok")
#assert (10<5),"this code is not ok" 

# exception handling
try:
    x=10/0
    print(x)

except ArithmeticError:
    print("arthimetic exception occured")
except :
    print("other exception")
else:
    print("no exception")
finally:
    print("always run")