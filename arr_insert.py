import array

def insertion_sort(array):
    for i in range(1,len(array)):
        j=i-1
        anchor = array[i]
        while j>=0 and anchor < array[j]:
            array[j+1]=array[j]
            j=j-1
        array[j+1]=anchor




n=int(input("please enter the size of array \n"))
pratik=array.array('i',[])
for i in range(n):
    pratik.append(int(input()))    


insertion_sort(pratik)
print(pratik)



