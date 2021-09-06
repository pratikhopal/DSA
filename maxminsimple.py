import array 

def maxelement(array):
    maxnum=-10000000
    for i in range(len(array)):
        if array[i]>maxnum:
            maxnum=array[i]
    print(maxnum,"is the maximum element in the array\n")

def minelement(array):
    minnum=1000000
    for i in range(len(array)):
        if array[i]<minnum:
            minnum=array[i]
    print(minnum,"is the minimum element in the array\n")




n=int(input("please enter the size of array\n"))
arr=array.array('i',[])
for i in range(n):
    arr.append(int(input()))


maxelement(arr)
minelement(arr)

