#Write a function that returns true if the given Binary Tree is SumTree 
# else false. A SumTree is a Binary Tree where the value of a node is equal 
# to the sum of the nodes present in its left subtree and right subtree.
#  An empty tree is SumTree and the sum of an empty tree can be 
# considered as 0. A leaf node is also considered as SumTree.
class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def checkSum(root):
    left_sum = 0
    right_sum = 0
    if root is None or root.left is None and root.right is None :
        return True
    if root.left is not None:
        left_sum+= root.left.data

    if root.right is not None:
        right_sum+= root.right.data
    
    if root.data == left_sum+right_sum and checkSum(root.right)!=False and checkSum(root.left)!=False:
        return True
    else:
        return False


#Another way of checking the sum tree or not

#checking it is leaf or not
def isLeaf(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return 0

#checking the sum property
def checkSum2(root):
    ls= 0
    rs= 0
    if root is None or isLeaf(root):
        return 1
    if checkSum2(root.left) and checkSum2(root.right) :
        if root.left is None:
            ls = 0
        elif isLeaf(root.left):
            ls = root.left.data
        else:
            ls = 2*(root.left.data)
        if root.right is None:
            rs = 0
        elif isLeaf(root.right):
            rs = root.right.data
        else:
            rs = 2*(root.right.data)
        return  root.data == ls+rs
    return 0


root =None
root = node(10)
root.left = node(8)
root.right = node(2)
root.left.left = node(3)
root.left.right = node(5)
root.right.right = node(2)
 
    # Function call
if(checkSum2(root)):
    print("The given tree satisfies the",
              "children sum property ")
else:
    print("The given tree does not satisfy",
          "the children sum property ")
