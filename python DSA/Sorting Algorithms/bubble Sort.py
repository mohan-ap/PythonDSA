arr=[20,30,40,10,50]

def bubbleSort(arr):
    temp=0
    n=len(arr)
    for i in range(n):
        for j in range(0,n-1):
            if(arr[j]>arr[j+1]):
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                #arr[j], arr[j + 1] = arr[j + 1], arr[j]  #for swapping
print("Before sorting")
print(arr)
bubbleSort(arr)
print("after sorting")
print(arr)


