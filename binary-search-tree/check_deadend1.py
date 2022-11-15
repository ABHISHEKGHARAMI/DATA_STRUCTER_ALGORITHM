#Simple Recursive solution to check whether BST contains dead end
#Given a Binary Search Tree that contains positive integer values greater than 0. 
# The task is to check whether the BST contains a dead end or not. Here Dead End means, we are not able to insert 
# any integer element after that node.
import sys
class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def insert(root,data):
    if root==None:
        return node(data)
    else:
        if(root.data < data):
            root.right = insert(root.right,data)

        else:
            root.left = insert(root.left,data)
    return root

#inorder traversal 
def inOrder(root):
    if root!=None:
        inOrder(root.left)
        print(root.data,end=" ")
        inOrder(root.right)

def check_deadEnd(root,min,max):
    if root==None:
        return False
    if min == max:
        return True
    return check_deadEnd(root.left,min,root.data-1) or check_deadEnd(root.right,root.data+1,max)

root = None
root = insert(root, 8);
root = insert(root, 5);
root = insert(root, 2);
root = insert(root, 3);
root = insert(root, 7);
root = insert(root, 11);
root = insert(root, 4);

if check_deadEnd(root,1,99)==True:
    print("The tree has dead end.")
else:
    print("The tree don't contain any dead end..")

