#Given the binary Tree and the two nodes say ‘a’ and ‘b’, determine whether the two nodes are
#  cousins of each other or not.
#Two nodes are cousins of each other if they are at same level and have different parents.

from platform import node


class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

#inorder
def inOrder(root):
    if root is not None:
        inOrder(root.left)
        print(root.data,' << ')
        inOrder(root.right)

def level(root,ptr,lev):
    if root is None:
        return 0
    if root==ptr:
        return lev
    l = level(root.left,ptr,lev+1)
    if l!=0:
        return l
    return level(root.right,ptr,lev+1)

#is siblings
def isSiblings(root,a,b):
    if root is None:
        return 0
    return (root.left==a and root.right==b) or (root.left==b and root.right == a) or isSiblings(root.left,a,b) or isSiblings(root.right,a,b)

# cousin
def isCousin(root,a,b):
    if root is None:
        return 0
    if (level(root,a,1)== level(root,b,1)) and not isSiblings(root,a,b):
        return 1
    else:
        return 0

#insert data
root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.left.right.right = node(15)
root.right.left = node(6)
root.right.right = node(7)
root.right.left.right = node(8)

node1 = root.left.right
node2 = root.right.right

print('Yes' if isCousin(root,node1,node2)==1 else 'No')


