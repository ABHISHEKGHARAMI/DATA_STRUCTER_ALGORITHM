#We have a binary search tree and a number N. 
# Our task is to find the greatest number in the binary search tree that is less than or equal to N.
#  Print the value of the element if it exists otherwise print -1.
class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def insert(root,data):
    if root==None:
        return node(data)
    else:
        if root.data < data:
            root.right = insert(root.right,data)
        else:
            root.left = insert(root.left,data)
    return root

def inOrder(root):
    if root!=None:
        inOrder(root.left)
        print(root.data,end=" ")
        inOrder(root.right)


#check for the largest of n of a given tree
def check_big(root,n):
    if root==None:
        return -1
    if root.data == n:
        return n
    elif root.data < n:
        k = check_big(root.right,n)
        if k==-1:
            return root.data
        else:
            return k
    elif root.data > n:
        return check_big(root.left,n)
root=None
root =  insert(root, 25)
root =    insert(root, 2)
root=   insert(root, 1)
root=    insert(root, 3)
root=   insert(root, 12)
root =     insert(root, 9)
root=   insert(root, 21)
root=    insert(root, 19)
root=    insert(root, 25)
inOrder(root)
print("\n")
print(check_big(root,4))

