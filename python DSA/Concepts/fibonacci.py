def fibonacci(length):
    first,second=0,1
    print(first, second, end=" ")
    length=length-2
    while length>0:
        print(first+second, end=" ")
        temp=second
        second=first+second
        first=temp
        length=length-1
    print()

length=int(input("enter number you want to print in the fibonacci series "))
fibonacci(length)

#using recursion

def fibonacci(first,second,length):
    if length>0:
        print(first+second, end=" ")
        temp=second
        second=first+second
        first=temp
        return fibonacci(first,second,length-1)
    else:
        exit()

length=int(input("enter number you want to print in the fibonacci series "))
first,second=0,1
print(first,second,end=" ")
length=length-2
fibonacci(first,second,length)
