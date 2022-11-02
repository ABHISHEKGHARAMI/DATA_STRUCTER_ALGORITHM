#A full binary tree is defined as a binary tree in which all nodes have either zero or two child nodes.
#  Conversely, there is no node in a full binary tree, which has one child node
class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def isFullTree(root):
    if root == None:
        return True
    if root.left == None and root.right == None:
        return True
    if root.left!=None and root.right!=None:
        return True
    if root.left!=None and root.right!=None:
        return isFullTree(root.left) and isFullTree(root.right)
    return False


root = node(10)
root.left = node(20)
root.right = node(30)

root.left.right = node(40)
root.left.left = node(50)
root.right.left = node(60)
root.right.right = node(70)

root.left.left.left = node(80)
root.left.left.right = node(90)
root.left.right.left = node(80)
root.left.right.right = node(90)
root.right.left.left = node(80)
root.right.left.right = node(90)
root.right.right.left = node(80)
root.right.right.right = node(90)


if isFullTree(root) == True:
    print("Full Binary Tree.")
else:
    print("Not a FullBinary Tree.")