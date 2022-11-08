#Find k-th smallest element in BST
#Given the root of a binary search tree and K as input, find Kth smallest element in BST.
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

def inOrder(root):
    if root!=None:
        inOrder(root.left)
        print(root.data,end=" ")
        inOrder(root.right)

# kth smallest
def kth_smallest(root,k):
    if root==None:
        return None
    left = kth_smallest(root.left,k)
    if left!=None:
        return left
    k=k-1
    if k==0:
        return root
    return kth_smallest(root.right,k)


root = None
keys = [20, 8, 22, 4, 12, 10, 14]

for x in keys:
    root = insert(root, x)

inOrder(root)

k = 2
print("\n")
print("The kth smallest node in the tree :",kth_smallest(root,k).data)
    
    