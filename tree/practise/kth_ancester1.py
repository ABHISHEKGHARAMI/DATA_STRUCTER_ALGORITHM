#print all the ancester of a given tree of a node
class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def ancester(root,n,num):
    if root:
        path = []
        ancester_util(root,path,n)

        if len(path)>0:
            return path[len(path)-num-1]
    else:
        return -1

def ancester_util(root,path,n):
    if root== None:
        return False
    path.append(root.data)
    if root.data == n:
        return True
    if root.left!=None and ancester_util(root.left,path,n) or root.right!=None and ancester_util(root.right,path,n):
        return True
    path.pop()
    return False
def ance1(root,n):
    if root==None:
        return  False
    if root.data == n:
        return True
    if ance1(root.left,n) or ance1(root.right,n):
        print(root.data,end=" ")
        return True
    return False
#main

root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
 
path = ancester(root,5,2)
if path!=-1:
    print(path)
else:
    print("No ancester...")
ance1(root,7)