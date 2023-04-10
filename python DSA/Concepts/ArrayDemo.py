import array

#integer type array
'''arr=array.array('i',{1,2,3,4,5})
print(arr)
print(arr[0])
arr[2]=30
print(arr)
print(len(arr))'''

#character type array

'''arr=array.array("u",['m','o','h','a','n'])
print(arr)'''


arr=array.array("c",['moh'])
print(arr)


#string to character array

'''s="mohankumar"
arr=array.array("b",list(s.encode())) # returns ascii values
print(arr)'''

'''s="mohankumar"
arr=array.array("",list(s))
print(arr)
for i in range(len(arr)):
    if(arr[i]=='m' or arr[i]=='k'):
        print(arr[i],end="")
print()'''

#float type array

"""arr=array.array("f",{1.1,1.2,1.3})
print(arr)
print(arr[1])"""

#double type array

'''arr=array.array("i",{1.2,2.3,3.4,4.5})
print(arr)'''
