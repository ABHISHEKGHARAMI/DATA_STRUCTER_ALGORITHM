# find the distance between two nodes of given tree
class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def distance(root,n1,n2):
    if root:
        path1 = []
        distance_utill(root.left,path1,n1)

        path2 = []
        distance_utill(root.right,path2,n2)

        i = 0
        while i < len(path1) and i < len(path2):
            if path1[i]!=path2[i]:
                break
            i+=1
        return len(path1) + len(path2) -2*i
    else:
        return -1

def distance_utill(root,path,n):
    if root== None:
        return False
    path.append(root.data)
    if root.data == n:
        return True
    if root.left!=None and distance_utill(root.left,path,n) or root.right!=None and distance_utill(root.right,path,n):
        return True
    path.pop()
    return False


root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.right.right = node(7)
root.right.left = node(6)
root.left.right = node(5)
root.right.left.right = node(8)

dist = distance(root, 4, 5)
print("Distance between node {} & {}: {}".format(4, 5, dist))

dist = distance(root, 4, 6)
print("Distance between node {} & {}: {}".format(4, 6, dist))

dist = distance(root, 3, 4)
print("Distance between node {} & {}: {}".format(3, 4, dist))

dist = distance(root, 2, 4)
print("Distance between node {} & {}: {}".format(2, 4, dist))

dist = distance(root, 8, 5)
print("Distance between node {} & {}: {}".format(8, 5, dist))
