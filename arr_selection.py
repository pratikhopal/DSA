import array


def selection_sort(array):
    for i in range(0,len(array)-1):
        minpos=i
        for j in range(i,len(array)):
            if array[j]<array[minpos]:
                minpos=j
        temp = array[i]
        array[i]=array[minpos]
        array[minpos]=temp
    print(array)





n=int(input("please enter the size of array\n"))
arr=array.array('i',[])
for i in range(n):
    arr.append(int(input()))

selection_sort(arr)
