#find the second largest element of the tree
class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def insert(root,data):
    if root== None:
        return node(data)
    if root.data < data:
        root.right = insert(root.right,data)
    elif root.data > data:
        root.left = insert(root.left,data)
    return root

def inOrder(root):
    if root!=None:
        inOrder(root.left)
        print(root.data,end=" ")
        inOrder(root.right)


def second_largest(root):
    c = [0]
    second_largestutill(root,c)

def second_largestutill(root,c):
    if root==None or c[0]>1:
        return
    second_largestutill(root.right,c)
    c[0]+=1
    if c[0]==2:
        print("{} th largest element is : {}".format(2,root.data))
        return
    return second_largestutill(root.left,c)


root = None

arr = [50,20,30,40,70,60,80]

for i in arr:
    root = insert(root,i)
inOrder(root)
second_largest(root)
