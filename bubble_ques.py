#Given an Integer N and a list arr. Sort the array using bubble sort algorithm

import array

def bubblesort(array):
    size=len(arr)
    for  j in range(size-1):
        for i in range(size-1):
            if arr[i]>arr[i+1]:
                temp=arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=temp
    print(arr)



n = int(input("enter the size of the array\n"))
arr=array.array('i',[])
for i in range(n):
    arr.append(int(input()))

bubblesort(arr)

