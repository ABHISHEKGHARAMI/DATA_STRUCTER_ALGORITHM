# Write a function that returns true if the given Binary Tree is SumTree else false.
#  A SumTree is a Binary Tree where the value of a node is equal to the sum of the nodes present 
# in its left subtree and right subtree. An empty tree is SumTree and the sum of an empty tree can be considered as 0.
#  A leaf node is also considered as SumTree.
class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def sum(root):
    if root is None:
        return 0
    else:
        return root.data + sum(root.left) + sum(root.right)

def check_Sumtree(root):
    ls,rs = 0,0
    if root==None or root.left == None and root.right == None:
        return 1
    ls = sum(root.left)
    rs = sum(root.right)
    if root.data == ls+rs and check_Sumtree(root.left) and check_Sumtree(root.right):
        return 1
    return 0

# this is O(n^2) time worst case
def leaf(root):
    if root== None:
        return 0
    if root.left == None and root.right == None:
        return 1
    return 0
#sumtree for the check
def check_Sum(root):
    if root == None or leaf(root):
        return 1
    if check_Sum(root.left) and check_Sum(root.right):
        if root.left == None:
            ls = 0
        elif leaf(root.left):
            ls = root.left.data
        else:
            ls = 2*(root.left.data)
        if root.right == None:
            rs = 0
        elif leaf(root.right):
            rs = root.right.data
        else:
            rs = 2*(root.right.data)
        return root.data==ls+rs
    return 0
root = node(26)
root.left= node(10)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(6)
root.right.right = node(3)

print(' Sum Tree .' if check_Sumtree(root)==1 else ' Not a Sum Tree .')
print('Sum Tree..' if check_Sum(root)==1 else 'Not Sum Tree.')