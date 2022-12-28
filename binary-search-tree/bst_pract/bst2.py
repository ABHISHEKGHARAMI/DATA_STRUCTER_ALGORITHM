#binary search tree
class tree:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
def insert(root,data):
    if root is None:
        return tree(data)
    else:
        if root.data == data:
            return root
        if root.data < data:
            root.right = insert(root.right,data)
        else:
            root.left = insert(root.left,data)
    return root
#search in binary tree
def search(root,data):
    if root==None:
        return False
    else:
        if root.data == data:
            return True
        elif root.data < data:
            return search(root.right,data)
        else:
            return search(root.left,data)
#display the data
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)
#get the min value
def minValue(root):
    curr = root
    while curr.left:
        curr = curr.left
    return curr
#delete the node from the tree
def delete(root,data):
    if root==None:
        return root
    else:
        if root.data < data : 
            root.right = delete(root.right,data)
        elif root.data > data:
            root.left = delete(root.left,data)
        else:
            if root.left ==None:
                temp = root.right
                return temp
            elif root.right == None:
                temp = root.left
                return temp
            else:
                temp = minValue(root.right)
                root.data = temp.data
                root.right = delete(root.right,temp.data)
    return root

#floor of the tree
def floor(root,x):
    res = None
    while root!=None:
        if root.data == x:
            return root
        elif root.data > x:
            root = root.left
        else:
            res= root
            root = root.right
    return res
#ceiling of a given tree
def ceil(root,x):
    res = None
    while root!=None:
        if root.data == x:
            return root
        elif root.data < x:
            root = root.right
        else:
            res = root
            root = root.left
    return res
#height of a binary tree
def height(root):
    if root==None:
        return 0
    else:
        lheight = height(root.left)
        rheight = height(root.right)
        return max(lheight,rheight)+1
#check it is abinary tree
def check_btree(root):
    if root == None:
        return True
    else:
        if root.data < root.right.data and root.data > root.left.data:
            return True
        else:
            return check_btree(root.left) and check_btree(root.right)

#find the kth smallest element in the binary search tree
def kth_smallest(root,k):
    if root==None:
        return None
    left = kth_smallest(root.left,k)
    if left!=None:
        return left
    k=k-1
    if k==0:
        return root
    return kth_smallest(root.right,k)

root = tree(20)
arr = [15 , 30 ,40 , 50, 12, 18,35,7,40]
for i in range(len(arr)):
    insert(root,arr[i])
print("The inorder traversal of the tree as follow:",end=" ")
inorder(root)
if(search(root,40)==True):
    print("\nThe value is present...")
else:
    print("\nThe value is not present in the tree....")
#delete(root,20)
#inorder(root)
print("The floor of the data is : ",floor(root,48).data)
print("The floor of the bianry tree is : ",ceil(root,19).data)
print("The height odf the binary tree is :",height(root))
if(check_btree(root)==False):
    print("Not a Binary tree..")
else:
    print("A binary tree..")
print("The kth smallest element of the binary tree : ",kth_smallest(root,2).data)


