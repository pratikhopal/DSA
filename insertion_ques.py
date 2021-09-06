#implement Insertion Sort and sort the array entered from the user.
import array

def insert(array):
    for i in range(1,len(array)):
        anchor=array[i]
        j=i-1
        while j>=0 and anchor<array[j]:
            array[j+1]=array[j]
            j=j-1
        array[j+1]=anchor

    print(array)



n = int(input("enter the size of array \n"))
arr=array.array('i',[])
for i in range(n):
    arr.append(int(input()))

insert(arr)
