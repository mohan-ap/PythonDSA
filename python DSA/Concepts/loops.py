#while loop
'''def main():
    i=1
    while(i<5):
        print(i)
        i=i+1
       
    else:
        print("condition false")
main()'''

#for loop

'''for i in range(1,5):
    print(i,end=" ")
    
else:
    print()
    print("condition false")

'''

#nested for loops
count=5
for i in range(1,5):
    for j in range(1,count):
        print("*",end="")
    print()
    count=count-1