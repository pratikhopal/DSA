#A tree is called full when every node has 0 or 2 child nodes
#A tree is called perfect when every node has 2 child nodes
#A tree is called complete where a tree is filled from left to right.
class Node:
    def __init__(self,value):
        self.value = value 
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if temp.value == new_node.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
            









mytree = BinarySearchTree()
mytree.insert(2)
mytree.insert(1)
mytree.insert(3)
print(mytree.root.value)
print(mytree.root.left.value)
print(mytree.root.right.value)

