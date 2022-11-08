# check this is BST or not
import sys
max1 = sys.maxsize
min1 = -sys.maxsize
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def check_Bst(root):
    return bst_utill(root,min1,max1)

def bst_utill(root,min,max):
    if root==None:
        return True
    if root.data < min or root.data > max:
        return False
    else:
        return bst_utill(root.left,min,root.data-1) and bst_utill(root.right,root.data+1,max)


root = node(4)
root.left = node(2)
root.right = node(5)
root.left.left = node(1)
root.left.right = node(3)
print(check_Bst(root))