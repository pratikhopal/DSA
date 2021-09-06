class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def printlist(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

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

       
    def get(self, index):
        if index < 0 or index >= self.length:   #if the index is less than zero or greater than length
            return None                         #return zero
        temp = self.head            #else put the head in temp
        for _ in range(index):      #run a loop till the index 
            temp = temp.next        #store the indexth node in temp
        return temp        #now return the value of the node (always return the node itself not the value)


   

my_linkedlist=LinkedList(11)
my_linkedlist.append(12)
my_linkedlist.append(13)
my_linkedlist.append(14)
my_linkedlist.append(15)
my_linkedlist.printlist()
