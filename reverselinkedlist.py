class Node:
    def __init__(self,value):
        self.value = value
        self.next=None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def printlist(self):
        temp = self.head
        while temp is not None:
            print(temp.value) 
            temp=temp.next
    
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length = self.length + 1

    def reverselist(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp 
        after = temp.next
        before = None
        for _ in range (self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
    

mylist=LinkedList(10)
mylist.append(20)
mylist.append(30)
mylist.append(40)
mylist.append(50)
mylist.reverselist()
mylist.printlist()