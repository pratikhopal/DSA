#program for adding new nodes in our linkedlist in the tail
#so at first i will create a new linkedlist
#creating a class to create nodes
class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

#now creating a class to create for our linkedlist
class LinkedList:


    #constructor to initiate linkedlist
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1


    #method to print our linkedlist
    def printlist(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
    

    #now lets create a method to append new node to our linked list
    def append(self,value):
        naya_node=Node(value)       #so we create a node with value
        if self.head is None:       #we check if our linkedlist is empty
            self.head=naya_node     #if empty we put our only node as head and tail both
            self.tail=naya_node
        else:                        #else 
            self.tail.next=naya_node #we we point the last node of our list to new node
            self.tail=naya_node      #and make our newly added node as the tail
        self.length=self.length+1    #and finally increase the length of our list
        return True



my_linked_list=LinkedList(40)
my_linked_list.append(35)
my_linked_list.append(55)
my_linked_list.append(65)
my_linked_list.append(75)
my_linked_list.printlist()






