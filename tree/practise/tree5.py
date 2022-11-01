#Given a binary tree, you need to check whether sum of all
#  covered elements is equal to sum of all uncovered elements
#  or not.
#In a binary tree, a node is called Uncovered if it appears 
# either on left boundary or right boundary. 
# Rest of the nodes are called covered.
class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
#inorder
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
def sum(root):
    if root is None:
        return 0
    else:
        return root.data+sum(root.left)+sum(root.right)

#under cover  left
def undercoverSum_left(root):
    if root.left== None and root.right == None:
        return root.data
    if root.left!=None:
        return undercoverSum_left(root.left)
    else:
        return undercoverSum_left(root.right)

#under cover right
def undercoverSum_right(root):
    if root.left== None and root.right == None:
        return root.data
    if root.right!=None:
        return undercoverSum_right(root.right)
    else:
        return undercoverSum_right(root.left)
#under cover sum
def undercoverSum(root):
    lb = 0 
    rb = 0
    if root.left!=None:
        lb = undercoverSum_left(root.left)
    if root.right!= None:
        rb = undercoverSum_right(root.right)

    return root.data + lb + rb

# check the both sum
def check(root):
    sumUC = undercoverSum(root)

    sumT = sum(root)

    if (sumUC == (sumT - sumUC)):
        return 1
    else:
        return 0 
#testing
root =node(8)
root.left =node(3)

root.left.left =node(1)
root.left.right =node(6)
root.left.right.left =node(4)
root.left.right.right =node(7)

root.right =node(10)
root.right.right =node(14)
root.right.right.left =node(13)
print("The sum of the tree is : ",sum(root))
print("The under cover sum is : ",undercoverSum(root))
if check(root)==1:
    print("The both sum matches.")
else:
    print("Does not matches..")

