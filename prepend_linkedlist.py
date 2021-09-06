class Node():
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList():
    
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1
    
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length=self.length+1
        return True

    def printlist(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def prepend(self,value):                        
        new_node=Node(value)                                #we create a node 
        if self.head is None:                               #we check is our head pointer is none if yes 
            self.head=new_node                              #we make our new node as head and tail both 
            self.tail=new_node
        else:
            new_node.next=self.head    #else we give our next pointer of new node the address of  previous head node
            self.head=new_node         #and point our head pointer towards our new node making it head node                  
        self.length=self.length+1      #now we increase the length
        return True

mylinkedlist=LinkedList(10)
mylinkedlist.append(20)
mylinkedlist.append(30)
mylinkedlist.printlist()


print("/n ")
print("after prepending")
mylinkedlist.prepend(50)
mylinkedlist.printlist()
