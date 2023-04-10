arr=[10,20,30,40,50]

def binarySearch(arr,ele):
        low,high=0,len(arr)-1
        present=False
        while low<=high:
                mid=int((low+high)/2)  #explicit type casting if we perform divison 
                if arr[mid]==ele:          #operation automatically covert as float data type
                    print(f"Element present at the index {mid}")
                    present=True
                    break
                elif arr[mid]<ele:
                       low=mid+1
                       high=high
                else:
                       low=low
                       high=mid-1
        if present == False:
               print("Element not prsent in the list") 

print("Elements are")
print(arr)
x=int(input("enter an element to search "))     
binarySearch(arr,x)       
        
