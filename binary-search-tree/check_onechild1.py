#Given Preorder traversal of a BST, check if each non-leaf node has only one child. 
# Assume that the BST contains unique entries.
class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def insert(root,data):
    if root==None:
        return node(data)
    if root.data < data:
        root.right = insert(root.right,data)
    elif root.data > data :
        root.left = insert(root.left,data)
    return root
def inorder(root):
    if root!=None:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)

#check one child
def check_one_child(root):
    if root==None:
        return False
    if root.left is None and root.right is None:
        return False
    if root.left is None or root.right is None:
        return True
    return check_one_child(root.left) or check_one_child(root.right)


root = None
arr = [8, 3, 5, 7, 6]

for i in arr:
    root = insert(root,i)

inorder(root)

print(check_one_child(root))

