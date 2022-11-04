#find the common ancester between the two given nodes in a tree
class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def common_ancester(root,n1,n2):
    if root:
        path = []
        path1 = []
        common_ancester_util(root,path1,n1)

        path2 = []
        common_ancester_util(root,path,n2)

        i = 0
        while i < len(path1) and i<len(path2):
            if path1[i]==path2[i]:
                path.append(path1[i])
            i+=1
        return path
    else:
        return -1

def common_ancester_util(root,path,n):
    if root == None:
        return False
    path.append(root.data)
    if root.data == n:
        return True
    if root.left!=None and common_ancester_util(root.left,path,n) or root.right!=None and common_ancester_util(root.right,path,n):
        return True
    path.pop()
    return False

#main
root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(6)
root.right.right = node(7)
root.left.left.left = node(8)
root.right.left.left = node(9)
root.right.left.right = node(10)

path = common_ancester(root,9,7)
if path!=-1:
    print(path)
else:
    print("No common ancester..")