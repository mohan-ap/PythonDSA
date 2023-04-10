def insertionSort(arr):
    for i in range(1,len(arr)):
        j=i-1
        min=arr[i]
        while arr[j]>min and j>=0:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=min
arr=[40,30,50,20,10]
print("before sorting")
print(arr)
insertionSort(arr)
print("After sorting")
print(arr)


