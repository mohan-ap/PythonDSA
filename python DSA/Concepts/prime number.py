def primeNumber(num):
    
    for i in range(1,num+1):
        count=0
        for j in range(1,i+1):
            if i%j ==0:
                count=count+1
        if count==1 or count==2:
            print(i,end=" ")
    print()
x=int(input("please enter a number from 1 to any to print prime numbers "))     
primeNumber(x)    
    

