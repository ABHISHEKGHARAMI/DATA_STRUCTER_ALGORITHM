#Given a Binary Tree, write a function to check whether the given Binary Tree is a perfect Binary Tree or not.
#A Binary tree is Perfect Binary Tree in which all internal nodes have two children and all leaves are at same level.
class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def depth(root):
    d= 0 
    while root!=None:
        root = root.left
        d+=1
    return d

def isPerfectutil(root,d,level=0):
    if root==None:
        return True
    if root.left==None and root.right==None:
        return d==level+1
    if root.left==None or root.right==None:
        return False
    return isPerfectutil(root.left,d,level+1) and isPerfectutil(root.right,d,level+1)

def isPerfect(root):
    d = depth(root)
    if isPerfectutil(root,d)==True:
        return 1
    else:
        return 0

root = None
root = node(10)
root.left = node(20)
root.right = node(30)
 
root.left.left = node(40)
root.left.right = node(50)
root.right.left = node(60)
root.right.right = node(70)

if isPerfect(root)==1:
    print("Perfect Tree.")
else:
    print("Not a Perfect Tree.")    
