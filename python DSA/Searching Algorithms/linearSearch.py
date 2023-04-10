arr=[10,20,30,40,50]

def linearSearch(arr,ele):
    present=False
    for i in range(0,len(arr)):
        if(arr[i]==ele):
            print(f"Element is in the index {i}")
            present=True
            break
    if present == False:
        print("element not present in the array")
print("Array elements are ")
print(arr)
ele=int(input("enter an element to search "))
linearSearch(arr,ele)