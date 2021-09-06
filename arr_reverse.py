import array
def array_reverse(arr,n):
    start =0
    end=n-1
    while start<end:
        temp=arr[start]
        arr[start]=arr[end]
        arr[end]=temp
        start=start+1
        end=end-1
    print(arr)

n=int(input())
arr=array.array('i',[])
for i in range (0,n):
    arr.append(int(input())) 




a=20
b=10
print(a,b)
a=a+b
b=a-b
a=a-b
print(a,b)