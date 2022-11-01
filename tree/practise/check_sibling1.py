#python program to check to node are sibling or not
class node:
    def __init__(self,data):
        self.data = data
        self.left =None
        self.right = None

def isSibling(root,a,b):
    if root is None:
        return 0

    if root.left == a and root.right == b or isSibling(root.left,a,b) or isSibling(root.right,a,b):
        return 1
    else:
        return 0


root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.left.right.right = node(15)
root.right.left = node(6)
root.right.right = node(7)
root.right.left.right = node(8)

node1 = root.left.left
node2 = root.left.right

print('yes' if isSibling(root,node1,node2)==1 else 'no')