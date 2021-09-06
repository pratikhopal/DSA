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

    def printlist(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next        

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

    def pop(self):
        if self.length==0:
            return None
        pre = self.head
        temp=self.head
        while temp.next is not None:
            pre = temp
            temp=temp.next
        self.tail=pre
        self.tail.next=None
        self.length-=1
        if self.length==0:
            self.head=None
            self.tail=None
        return temp


    def popfirst(self):                    
        if self.length==0:               #if length is already is zero return none
            return None
        temp=self.head                  #put value of head pointer in temp 
        self.head=self.head.next        #put value of next pointer of head in head pointer thus making 2nd node head
        temp.next=None                  #since temp now has previous head node make its next pointer as none 
        self.length=self.length-1       #reduce the length by 1
        if self.length==0:
            self.tail=None



mylist=LinkedList(10)
mylist.append(20)
mylist.append(30)
mylist.printlist()
print("\n")
mylist.popfirst()
print("after first pop\n")
mylist.printlist()