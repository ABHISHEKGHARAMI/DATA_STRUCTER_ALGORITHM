#Given a binary tree, the task is to check for every node, its value is 
# equal to the sum of values of its immediate left and right child. 
# For NULL values, consider the value to be 0
class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def insert(root,data):
    if root is None:
        return node(data)
    if root.data < data :
        root.right = insert(root.right,data)
    else:
        root.left = insert(root.left,data)
    return root

#check sum properties
def check_sum(root):
    left_sum = 0
    right_sum = 0
    if root is None or root.left is None and root.right is None:
        return 1
    else:
        if root.left is not None:
            left_sum+=root.left.data

        if root.right is not None:
            right_sum+=root.right.data

        if root.data == left_sum+right_sum and check_sum(root.left)!=0 and check_sum(root.right)!=0:
            return 1
        else:
            return 0


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data,' << ',end=" ")
        inorder(root.right)   

root = None
arr = [2,8 ,10]
#for i in range(len(arr)):
    #root = insert(root, arr[i])
#inorder(root)
#v= check_sum(root)
#if v==1:
   # print("The tree follows check sum balance")
#else:
    #print("it does not.")
root = node(10)
root.left = node(8)
root.right = node(2)
root.left.left = node(3)
root.left.right = node(5)
root.right.right = node(2)
 
    # Function call
if(check_sum(root)):
    print("The given tree satisfies the",
              "children sum property ")
else:
    print("The given tree does not satisfy",
          "the children sum property ")
