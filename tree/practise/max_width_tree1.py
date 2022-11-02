#find the max width of the node 

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def getmaxwidth_utill(root,level):
    if root is None:
        return 0
    if level==1:
        return 1
    elif level>1:
        return getmaxwidth_utill(root.left,level-1)+getmaxwidth_utill(root.right,level-1)


def height(root):
    if root is None:
        return 0
    else:
        l = height(root.left)
        r = height(root.right)
        return max(l, r)+1
def getmaxwidth(root):
    h = height(root)
    max_width = 0
    for i in range(1,h+1):
        width = getmaxwidth_utill(root,i)
        max_width = max(max_width,width)
    return max_width




root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.right = node(8)
root.right.right.left = node(6)
root.right.right.right = node(7)
print("The max width is :",getmaxwidth(root))
