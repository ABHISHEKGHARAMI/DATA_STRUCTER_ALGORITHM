# lowest common ancester problem
# it will return the least root node for the given node
class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

#l-c-a function
def lca(root,n1,n2):
    path1 = []
    path2 = []
    if not lca_utill_bforce(root,path1,n1) or  not lca_utill_bforce(root,path2,n2):
        return -1
    i = 0
    while i < len(path1) and i < len(path2):
        if path1[i]!=path2[i]:
            break
        i+=1
    return path1[i-1]

# lca utill brute force
def lca_utill_bforce(root,path,n):
    if root==None:
        return False
    path.append(root.data)
    if root.data == n:
        return True
    if root.left!=None and lca_utill_bforce(root.left,path,n) or root.right!=None and lca_utill_bforce(root.right,path,n):
        return True
    path.pop()
    return False

#mian
root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(6)
root.right.right = node(7)
     
print("LCA(4, 5) = %d" % (lca(root, 4, 5,)))
print("LCA(4, 6) = %d" % (lca(root, 4, 6)))
print("LCA(3, 4) = %d" % (lca(root, 3, 4)))
print("LCA(2, 4) = %d" % (lca(root, 2, 4)))
print("LCA(5, 6) = %d" % (lca(root, 5, 6)))