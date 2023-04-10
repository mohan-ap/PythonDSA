import array as ar

arr=ar.array("i",[10,20,30,40,50])
print(arr)

length=len(arr) # to find the length of an array
print(f"Length of an array is {length}") #output=5

arr.append(60)  #to insert an element at end
print(arr)

arr.insert(2,35)  #to insert an element at specified index
print(arr)

arr.pop()  # deletes element at last 
print(arr)

arr.pop(2)  #removes element at the specified index
print(arr)

arr.remove(50)  #remove the specified element of first occurence
print(arr)

#to access an element 

print(arr[0])

#to change the value 
arr[1]=25
print(arr)

#to iterate an array
for i in range(len(arr)):
    print(arr[i])

#using while loop
i=0
while i<len(arr):
    print(arr[i])
    i=i+1

#sorting an array
'''arr.sort()
print(arr)                  #'array.array' object has no attribute 'sort'

#reverse sorting (descending order)
arr.sort(reverse=True)
print(arr)'''


#reverse in insertion order
arr.reverse()
print(arr)

#to find the index of specified element
print(arr.index(10))

#clear an array elements
'''arr.clear()           #'array.array' object has no attribute 'sort'
print(arr)'''


#copy an array elements to other variables

'''x=arr.copy(arr)   #'array.array' object has no attribute 'sort'
print(x)'''

#count the occurence of specified element

print(arr.count(10))

#combine two arrays

arr2=ar.array("i",[50,60,70,80])
arr.extend(arr2)
print(arr)