
# Implent a BST from scratch 


# Point of this exercise is 

# We don't want the user to interface with Node class at all 
class Node:
    def __init__(self, val):
        self.value = val
        self.leftChild = None 
        self.rightChild = None 

#Main interface for user 
class Tree:
    def __init__(self):
        self.root = None 

    def insert(self, data):
        if self.root:
            return self.root.insert(data)

        else:
            self.root = None(data)
            return True 



