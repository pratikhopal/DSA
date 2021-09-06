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

    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length=self.length+1

    def printlist(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next


    def get(self, index):
        if index < 0 or index > self.length:
            return None
        temp=self.head
        for _ in range (index):
            temp=temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length=self.length+1
        return True

    def insert_at_position(self,index,value):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp=self.get(index-1)
        new_node.next=temp.next
        temp.next=new_node
        self.length=self.length+1
        return True    






my_list=LinkedList(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.printlist()
print("\n")
my_list.set_value(2,35)
my_list.printlist()
print("\n")
my_list.insert_at_position(2,50)
my_list.printlist()
   