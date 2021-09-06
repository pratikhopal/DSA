#creating a linked list


#first we create a class to create nodes for our linked list
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

#now we create a class to create a linked list 

class LinkedList:
    def __init__(self,value):
        new_node=Node(value)  #we create a new_node using our Node class
        self.head=new_node    #we assign the new_node as head as it is the only node
        self.tail=new_node    #we assign the new_node as tail as it is the only node
        self.length=1         #we assign the new_node as length as 1 as it is the only node
    
    
    #method to print our linkedlist
    def printlist(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

my_linked_list=LinkedList(4)
my_linked_list.printlist()