class Node:
    def __init__(self,value):
        self.value=value
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
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length = self.length + 1

    def get_node(self,index):
        if index < 0 or index >= self.length:
            return None
        else:
            temp=self.head
            for _ in range (index):
                temp=temp.next
        return temp
    
    def pop_first(self):
        if self.head is None:
            return None
        else:
            temp=self.head
            self.head=self.head.next
            temp.next=None
            self.length = self.length - 1
            if self.length == 0:
                self.head=None
                self.tail=None

    def pop(self):
        if self.length == 0:
            return None
        pre = self.head
        temp = self.head

        while temp.next is not None:
            pre = temp
            temp=temp.next
        
        self.tail = pre
        self.tail.next = None
        self.length = self.length - 1
        if self.length == 0:
            self.head=None
            self.tail=None
        return temp

    def remove_at_index(self,index):
        if index < 0 or index > self.length:
            return None
        elif index == 0:
            self.pop_first()
        elif index == self.length -1 :
            self.pop()
        else:
            pre = self.get_node(index-1)
            temp = pre.next
            pre.next=temp.next
            temp.next=None
            self.length = self.length - 1
            return temp.value



mylist=LinkedList(10)
mylist.append(20)
mylist.append(30)
mylist.append(40)
mylist.append(50)
mylist.append(60)
mylist.printlist()
print(mylist.remove_at_index(3))