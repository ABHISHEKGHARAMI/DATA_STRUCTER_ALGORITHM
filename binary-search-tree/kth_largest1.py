#K’th Largest Element in BST when modification to BST is not allowed

class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def insert(root,data):
    if root==None:
        return node(data)
    if root.data < data :
        root.right = insert(root.right,data)
    elif root.data > data :
        root.left = insert(root.left,data)
    return root

def inOrder(root):
    if root!=None:
        inOrder(root.left)
        print(root.data,end=" ")
        inOrder(root.right)

def kth_largest_utill(root,k,c):
    if root==None or c[0]>=k:
        return
    kth_largest_utill(root.right,k,c)
    c[0]+=1
    if c[0]==k:
        print("{} largest node is : {}".format(k,root.data))
        return
    kth_largest_utill(root.left,k,c)

def kth_largest(root,k):
    c = [0]

    kth_largest_utill(root,k,c)

root = None

arr = [50 , 30, 20, 40, 70, 60, 80]

for i in arr:
    root = insert(root,i)

for i in range(1,8):
    kth_largest(root,i)
