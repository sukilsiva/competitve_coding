# Cisco Interview Question Taken from GeeksforGeeks
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class binarytree:
    # This Function is used to print the tree in reverse order
    # Here we are using recursion to traverse from last node
    # at level 1  printing the root 
    # and at higher levels printing the Childrens
    def print_function(self, root, level):
        if root is None:
            return 
        if level==1:
            print(root.val)
        if level > 1:
            self.print_function(root.left, level-1)
            self.print_function(root.right, level-1)        
    ### Function to know the height of a tree
    ### This will return the ,max of left and right because we need to traverse in reverse from 
    ### Max Height
    def height(self,root):
        if root is None:
            return 0
        l_height = self.height(root.left)
        r_height = self.height(root.right)
        if l_height > r_height:
            return l_height + 1
        else:
            return r_height + 1
    # This is an Main Function and Starting of the COde
    # Knowing the height of a tree
    # Traversing from reverse
    def reverseLevelOrder(self, root):
        if root == None:
            return 0
        h = self.height(root)
        for i in reversed(range(1, h+1)):
            self.print_function(root , i)

# Main Method 
if __name__ == "__main__":
    # binary tree initialization
    root = Node(1) 
    root.left = Node(2) 
    root.right = Node(3) 
    root.left.left = Node(4) 
    root.left.right = Node(5) 
    # Object for our class
    btr = binarytree() 
    print ("Level Order traversal of binary tree is{}".format(btr.reverseLevelOrder(root)) )