import array
def sort012(arr):
    for i in range (len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    print(arr)



n=int(input("enter the size of the input\n"))
arr=array.array('i',[])
for i in range (0,n):
    arr.append(int(input()))

sort012(arr)