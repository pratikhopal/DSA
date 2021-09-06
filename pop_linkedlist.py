class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    
    def __init__(self,value):
        node1=Node(value)
        self.head=node1
        self.tail=node1
        self.length=1

    def printlist(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
    
    def append(self,value):
        node2=Node(value)
        if self.head is None:
            self.head=node2
            self.tail=node2
        else:
            self.tail.next=node2
            self.tail=node2
        self.length=self.length+1

    def pop(self):
        if self.length==0:     #so we check if length of list is zero if so we return none
            return None
        pre =self.head        #we initialize a var pre with head pointer
        temp=self.head        #we initialize a var temp with head pointer pointing towards head node
        while temp.next is not None:      #now while next pointer of temp is not null we keep moving
            pre=temp                      #if temp.next is not null we put temp in pre
            temp=temp.next                ##if temp.next is not null we put temp.next in temp
        self.tail=pre               #so when we get node with next pointer as none and make previous node as tail 
        self.tail.next=None         #and make the last nodoes pointer as none
        self.length-=1              #also we decrease the length by -1
        if self.length==0:          #if our length of list becomes zero we make our pointers point to none
            self.head=None
            self.tail=None
        return temp   






my_list=LinkedList(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print("your linked list contains \n")
my_list.printlist()
print("after popping /n")
my_list.pop()
my_list.printlist()