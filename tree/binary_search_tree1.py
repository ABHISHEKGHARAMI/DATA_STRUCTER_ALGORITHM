#binary search tree
INT_MAX=4294967296
INT_MIN=-4294967296
class b_node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


    #insert the data in the tree
    def insert(self,key):
        if self.data<key:
            if self.right is None:
                self.right=b_node(key)
            else:
                self.right.insert(key)
        elif self.data>key:
            if self.left is None:
                self.left=b_node(key)
            else:
                self.left.insert(key)

    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.data,end=" ")
        if self.right is not None:
            self.right.inorder()


    def preorder(self):
        print(self.data)
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()

    def postorder(self):
        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()

def search(root,data):
    if root.data==data:
        return True
    elif root.data<data:
        return search(root.right,data)
    else:
        return search(root.left,data)
#delete the node from the tree
def delete_node(root,data):
    if root is None:
        return
    if root.data<data:
        root.right=delete_node(root.right,data)
    elif root.data>data:
        root.left=delete_node(root.left,data)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        temp=root.right
        temp_data=temp.data
        while temp.left:
            temp=temp.left
            temp_data=temp.data
        root.right=delete_node(root.right,root.key)
        return root

#find the minimum of the tree
def min_node(root):
    while root.left:
        root=root.left
    return root.data

#find the lowest common ancester of two given node
def find_path(root,path,k):
    if root is None:
        return False
    path.append(root.data)
    if root.data==k:
        return True
    if ((root.left!=None and find_path(root.left,path,k)) or (root.right!=None and find_path(root.right,path,k))):
        return True
    path.pop()
    return False
#lowest common ancester
def lowest_common_ans(root,n1,n2):
    path1=[]
    path2=[]
    if (not (find_path(root.left,path1,n1)) or (not find_path(root.right,path2,n2))):
        return -1
    i=0
    while i<len(path1) and i<len(path2):
        if path1[i]!=path2[i]:
            break
        i+=1
    return path1[i-1]
#check tree is binary or not
def isBST(node):
    return (isBSTUtil(node, INT_MIN, INT_MAX))
 
# Retusn true if the given tree is a BST and its values
# >= min and <= max
def isBSTUtil(node, mini, maxi):
     
    # An empty tree is BST
    if node is None:
        return True
 
    # False if this node violates min/max constraint
    if node.data < mini or node.data > maxi:
        return False
 
    # Otherwise check the subtrees recursively
    # tightening the min or max constraint
    return (isBSTUtil(node.left, mini, node.data -1) and
          isBSTUtil(node.right, node.data+1, maxi))


#find the kth smallest element of the tree
def kthsmallest(root):
    global k
    if root is None:
        return None
    left=kthsmallest(root.left)
    if left!=None:
        return left
    k=-1
    if k==0:
        return root
    return kthsmallest(root.right)
def print_kth(root):
    res=kthsmallest(root)
    if res is None:
        print("\nNo small element in there.")
    else:
        print("\nThe kth smallest element in there is :",res.data)
 


    





m=int(input("\nenter the root of the tree:"))
t1=b_node(m)
while True:
    print("\n1:insert. \t 2:inorder. \t 3:preorder. \t 4:postorder. \t 5:search.\t 6:delete. \t 7:min node.")
    print("\n8:lowest common ancester. \t 9:Check for binary tree. \t 10:for kth smaleest element.\t0 for exit.")
    choice=int(input("\nenter choice:"))
    if choice==1:
        n=int(input("enter the data:"))
        t1.insert(n)
    elif choice==2:
        t1.inorder()
    elif choice==3:
        t1.preorder()
    elif choice==4:
        t1.postorder()
    elif choice==5:
        n=int(input("enter the data to search:"))
        search(t1,n)
    elif choice==6:
        n=int(input("\nenter the data to be delete :"))
        delete_node(t1,n)
    elif choice==7:
        print("\nThe minimum node of the tree is :",min_node(t1))
    elif choice==0:
        break
    elif choice==8:
        n1,n2=map(int,input("\nEnter two nodes :").split(","))
        print("\nThe lowest common ancester of the given node is :",lowest_common_ans(t1,n1,n2))
    elif choice==9:
        if isBST(t1):
            print("\nBST.")
        else:
            print("\n Not BST.")
    elif choice==10:
        k=int(input("\nenter the number of smallest element to be present there :"))
        print_kth(t1)
    else:
        print("\n Wrong choice ...")
        
        






            






        
