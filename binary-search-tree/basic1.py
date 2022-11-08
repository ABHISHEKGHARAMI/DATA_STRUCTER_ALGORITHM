#basic in binary search tree
class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data)
        inOrder(root.right)
#insert data
def insert(root,data):
    if root == None:
        return node(data)
    else:
        if root.data == data:
            return root
        elif root.data < data:
            root.right = insert(root.right,data)
        else:
            root.left = insert(root.left,data)
    return root

#search value
def search(root,data):
    if root==None:
        return False
    else:
        if root.data == data:
            return True
        elif root.data < data :
            return search(root.right,data)
        else:
            return search(root.left,data)

def min_value(root):
    curr =root
    while curr.left:
        curr =  curr.left
    return curr

#delete key
def delete(root,data):
    if root is None:
        return root
    if root.data < data:
        root.right = delete(root.right,data)
    elif root.data > data:
        root.left = delete(root.left,data)
    else:
        if root.left is None:
            temp = root.right
            root= None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        else:
            temp = min_value(root.right)
            root.data = temp.data
            root.right = delete(root.right,temp.data)
    return root
#levelorder traversal
def  height(root):
    if root==None:
        return 0
    else:

        l = height(root.left)
        r = height(root.right)

        return max(l,r)+1
def levelorder(root):
    h = height(root)
    for i in range(1,h+1):
        level_utill(root,i)
def level_utill(root,level):
    if root==None:
        return
    if level == 1:
        print(root.data,end=" ")
    elif level>1:
        level_utill(root.left,level-1)
        level_utill(root.right,level-1)
root = node(50)

ar = [ 40,60,20,30,10,70]
for  i in range(len(ar)):
    insert(root,ar[i])
inOrder(root)

