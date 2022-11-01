from tempfile import tempdir


class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

#insert
def insert(root,data):
    if root is None:
        return node(data)
    if root.data > data :
        root.left = insert(root.left,data)
    if root.data < data :
        root.right = insert(root.right,data)
    return root

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data,' << ',end=" ")
        inorder(root.right)
#min value
def minvalue(root):
    temp = root
    while temp.left:
        temp = temp.left
    return temp

#delete
def delete(root,data):
    if root is None:
        return
    if root.data > data :
        root.left = delete(root.left,data)
    elif root.data < data :
        root.right = delete(root.right,data)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        else:
            temp = minvalue(root.right)
            root.data = temp.data
            root.right = delete(root.right,temp.data)
    return root


root = None
arr = [8,3,1,6,7,10,14,4]
for i in range(len(arr)):
    root = insert(root,arr[i])

inorder(root)
print("\n")
root= delete(root,3)
inorder(root)