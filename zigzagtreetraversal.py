# This question was asked in Cisco Taken from Geeks For Geeks
"""
Input:

Write a function to print ZigZag order traversal of a binary tree. 
For the below binary tree the zigzag order traversal will be 1 3 2 7 6 5 4 

Output:

ZigZag Order traversal of binary tree is 
1 3 2 7 6 5 4 
"""
class Node:
    def __init__(self, val,left =None,right=None):
        self.val = val
        self.left =left
        self.right = right
# Here the idea is to create two stacks current level and next level 
# While Node is at particular point in a tree append Node val to current level
# we are pushing the next levels of a node from left to right
# if current level == 0 then swapping of Nodes is Done
class binarytree:
    def zigzag(self, root):
        # Base Case 
        if root is None: 
            return
    
        # Create two stacks to store current 
        # and next level 
        currentLevel = [] 
        nextLevel = [] 
    
        # if ltr is true push nodes from  
        # left to right otherwise from 
        # right to left 
        ltr = True
    
        # append root to currentlevel stack 
        currentLevel.append(root) 
    
        # Check if stack is empty 
        while len(currentLevel) > 0: 
            # pop from stack 
            temp = currentLevel.pop(-1) 
            # print the data 
            print(temp.val, " ", end="") 
    
            if ltr: 
                # if ltr is true push left  
                # before right 
                if temp.left: 
                    nextLevel.append(temp.left) 
                if temp.right: 
                    nextLevel.append(temp.right) 
            else: 
                # else push right before left 
                if temp.right: 
                    nextLevel.append(temp.right) 
                if temp.left: 
                    nextLevel.append(temp.left) 
    
            if len(currentLevel) == 0: 
                # reverse ltr to push node in 
                # opposite order 
                ltr = not ltr 
                # swapping of stacks 
                currentLevel, nextLevel = nextLevel, currentLevel 

if __name__ == "__main__":
    root = Node(1) 
    root.left = Node(2) 
    root.right = Node(3) 
    root.left.left = Node(7) 
    root.left.right = Node(6) 
    root.right.left = Node(5) 
    root.right.right = Node(4) 
    print("Zigzag Order traversal of binary tree is") 
    btr = binarytree()
    btr.zigzag(root) 
  
  