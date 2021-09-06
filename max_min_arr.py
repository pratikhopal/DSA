import array

def maxmin(arr):
    if arr[0]>arr[1]:
        max_value=arr[0]
        min_value=arr[1]
    else:
        max_value=arr[1]
        min_value=arr[0]
    for i in range (2,len(arr)):
        if arr[i]>max_value:
            max_value=arr[i]
        if arr[i]<min_value:
            min_value=arr[i]
    print("the maximum value in the array is ",max_value)
    print("the minimum value in the array is ",min_value)

size_array=int(input("enter the size of the array\n"))
arr=array.array('i',[])
for i in range (0,size_array):
    arr.append(int(input()))

maxmin(arr)