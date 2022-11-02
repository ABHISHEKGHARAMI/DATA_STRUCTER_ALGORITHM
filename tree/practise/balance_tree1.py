#check that a tree is balance or not
class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

#height
def height(root):
    if root is None:
        return 0
    else:
        l = height(root.left)
        r = height(root.right)
        return max(l,r)+1
def isBalance(root):
    if root is None:
        return True
    l = height(root.left)
    h = height(root.right)
    if abs(l-h)<=1 and isBalance(root.left) and isBalance(root.right):
        return True
    return False
#eff sol
def is_Balance(root):
    if root is None:
        return 0
    l = is_Balance(root.left)
    if l==-1:
        return -1
    r = is_Balance(root.right)
    if r== -1:
        return -1
    if abs(l-r) >1 :
        return -1
    else:
        return max(l,r)+1
#main
root = node(10)
root.left = node(5)
root.right = node(12)
print('Yes' if isBalance(root)==True else 'No')
print(is_Balance(root))
    