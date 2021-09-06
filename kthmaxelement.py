import array
def kthmaxelement(arr,k):
    size=len(arr)
    for i in range(size-1):
        for j in range (size-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    min_element=arr[k-1]
    print(arr)
    print(min_element)


n=int(input("enter the size of array\n"))
arr=array.array('i',[])
for i in range (0,n):
    arr.append(int(input()))

k=int(input("enter the kth number to find\n"))
kthmaxelement(arr,k)