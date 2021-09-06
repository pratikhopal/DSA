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
        return True

    
    def get(self,index):
            if index < 0 or index > self.length:
                return None
            temp=self.head
            for _ in range(index):
                temp=temp.next
            return temp

    

    def printlist(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    

my_list=LinkedList(10)
my_list.append(20)
my_list.append(20)
my_list.append(40)
my_list.printlist()
print("\n")
my_list.set_value(2,30)
my_list.printlist()
