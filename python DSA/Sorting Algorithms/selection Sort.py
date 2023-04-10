arr=[20,30,40,10,50]

def selectionSort(arr):
    n=len(arr)
    temp=0
    for i in range(0,n-1):
        min=arr[i]
        pos=i
        for j in range(i+1,n): 
            if min>arr[j]:
                min=arr[j]
                pos=j
        temp=arr[i]
        arr[i]=min
        arr[pos]=temp

print("Before sorting")
print(arr)
selectionSort(arr)
print("after sorting")
print(arr)
