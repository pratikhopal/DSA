#binary search

import array
#function to do binary search
def binary_search(numbers_list, number_to_find):
    #initiliazing index left_index which is start index of the array, right_index which is the end of array 
     
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    #using the while loop to the condition that left_index is equal to right_index  
    while left_index <= right_index:
        #set the mid_index by adding the first and last index and dividing the two and getting the mid_index
        mid_index = (left_index + right_index) // 2
        #getting the middle element from the array using the mid_index
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find: #if the number we are finding is equal to mid_number return its index
            return mid_index

        if mid_number < number_to_find: #if the number we are finding is less than mid_number make its index 
            left_index = mid_index + 1  #as the left_index
        else:
            right_index = mid_index - 1 #if the number we are finding is more than mid_number make its index
                                        #as the right_index
    return -1






arr=array.array('i',[2,3,4,5,6,7,8,9,10])
number=int(input("enter the number to be found\n"))
print("the number you wanted to search was found at ",binary_search(arr,number))



"""

def binarysearch(array,num_to_find):
    start=0
    end=(len(array)-1)
    while start<=end:
        mid = (start + end)//2
        pivot=array[mid]
        if num_to_find == pivot:
            return mid 
        if num_to_find > pivot:
            start=mid+1
        else:
            end=mid-1
    return -1
"""