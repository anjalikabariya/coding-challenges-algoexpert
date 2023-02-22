'''Write a function that takes in a Binary Search Tree (BST) and a target integer value and returns the closest
value to that target value contained in the BST.
You can assume that there will only be one closest value.
Each BST node has an integer value , a left child node, and a right child node. A node is said to
be a valid BST node if and only if it satisfies the BST property: its value is strictly greater than the
values of every node to its left; its value is less than or equal to the values of every node to its right; and
its children nodes are either valid BST nodes themselves or None / null .
Sample Input
tree = 
           10
         /    \
        5     15
       / \    / \
      2  5   13 22
     /         \
    1          14

target = 12

Sample Output
13'''

def findClosestValueInBst(tree, target):
    # Write your code here.
    curr = tree
    closest = curr.value
    minDiff = abs(closest - target)
    
    while curr is not None:
        left = curr.left
        right = curr.right
        currDiff = abs(curr.value - target)
        if currDiff < minDiff:
            minDiff = currDiff
            closest = curr.value
        if curr.value > target:
            # traverse left
            curr = left
        elif curr.value < target:
            # traverse right
            curr = right
        else:
            break
    return closest
            
# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
