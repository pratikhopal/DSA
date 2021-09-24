class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Stack:
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def printstack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def push(self,value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height = self.height + 1


mystack = Stack(4)
mystack.push(5)
mystack.push(6)
mystack.push(7)
mystack.push(8)
mystack.printstack()