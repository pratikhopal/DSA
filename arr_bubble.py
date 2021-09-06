import array


arr=array.array('i',[5,9,4,10,8,6])

size=len(arr)
for j in range(size-1):
    for i in range(size-1):
        if arr[i]>arr[i+1]:
            temp=arr[i]
            arr[i]=arr[i+1]
            arr[i+1]=temp
print(arr)


