#creating the tree and insert the in the tree
class node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None


    #insert in the tree
    def insert(self,key):
        if self.key>key:
            if self.left is None:
                self.left=node(key)
            else:
                self.left.insert(key)
        elif self.key<key:
            if self.right is None:
                self.right=node(key)
            else:
                self.right.insert(key)
        else:
            self.key=key

    #inorder transformation
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.key,"->",end=" ")
        if self.right:
            self.right.inorder()

    def preorder(self):
        print(self.key,"->",end=" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    #postorder transformer
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.key,"->",end=" ")

#   # delete the node from the tree
def delete_Node(root, key):
  # if root doesn't exist, just return it
	if not root: 
		return root
	# Find the node in the left subtree	if key value is less than root value
	if root.key > key: 
		root.left = delete_Node(root.left, key)
	# Find the node in right subtree if key value is greater than root value, 
	elif root.key < key: 
		root.right= delete_Node(root.right, key)
	# Delete the node if root.value == key
	else: 
	# If there is no right children delete the node and new root would be root.left
		if not root.right:
			return root.left
	# If there is no left children delete the node and new root would be root.right	
		if not root.left:
			return root.right
  # If both left and right children exist in the node replace its value with 
  # the minmimum value in the right subtree. Now delete that minimum node
  # in the right subtree
		temp_val = root.right
		mini_val = temp_val.key
		while temp_val.left:
			temp_val = temp_val.left
			mini_val = temp_val.key
  # Delete the minimum node in right subtree
		root.right = delete_Node(root.right,root.key)
	return root


#find the height of the tree
def height(root):
    if root is None:
        return 0
    lheight=height(root.left)
    rheight=height(root.right)
    if lheight<rheight:
        return rheight+1
    else:
        return lheight+1
#level order traversal
def levelorder_traversal(root):
    h=height(root)
    for i in range(1,h+1):
        printlevelorder(root,i)

def printlevelorder(root,l):
    if root is None:
        return
    if l==1:
        print(root.key,end=" ")
    elif l>1:
        printlevelorder(root.left,l-1)
        printlevelorder(root.right,l-1)

#printing the min value in the tree
def min_val(root):
    curr=root.left
    val=curr.key
    while curr.left:
        curr=curr.left
        val=curr.key
    return val

#printing the max value in the tree
def max_val(root):
    curr=root.right
    while curr.right:
        curr=curr.right
    return curr.key


#search in the tree
def search(root,key):
    if root.key==key:
        return True
    elif root.key<key:
        return search(root.right,key)
    else:
        return search(root.left,key)

##check the sum for left and right sum its give the root node
def check_sum(root):
    left_sum=0
    right_sum=0
    if (root is None or (root.left is None and root.right is None)):
        return 1
    else:
        if root.left is None:
            right_sum+=root.key
        if root.right is None:
            left_sum+=root.key
        if (root.key==left_sum+right_sum and check_sum(root.left) and check_sum(root.right)):
            return 1
        else:
            return 0
#check the two node are they siblings
def is_sibling(root,a,b):
    if root is None:
        return 0
    return ((root.left==a and root.right==b) or(root.left==b and root.right==a) or
            is_sibling(root.left,a,b) or is_sibling(root.right,a,b))
    
#check the two node are cousine or not
def level(root,ptr,lev):
    if root is None:
        return 0
    if root==ptr:
        return lev
    l=level(root.left,ptr,lev+1)
    if l!=0:
        return l
    return level(root.right,ptr,lev+1)
#final function for checking the cousine or not
def check_cousine(root,a,b):
    if (level(root,a,1)==level(root,b,1) and is_sibling(root,a,b))==0:
        return 1
    else:
        return 0
#
#check for the leaf for same level
def check(root):
    level=0
    check.leaflevel=0
    return check_utill(root,level)
#for utill function
def check_utill(root,level):
    if root is None:
        return True
    if root.left is None and root.right is None:
        if check.leaflevel==0:
            check.leaflevel=level
            return True
        return level==check.leaflevel
    return check_utill(root.left,level+1)and (root.right,level+1)

##check sum tree or not
#sum tree is you sum its left subtree and right subtree gives roots data
def sum(root):
    if root is None:
        return 0
    return sum(root.left)+sum(root.right)+root.key
#check the sum tree
def check_sumtree(root):
    if root is None or root.left is None and root.right is None:
        return 1
    ls=sum(root.left)
    rs=sum(root.right)
    if root.key==ls+rs or check_sumtree(root.left) and check_sumtree(root.right):
        return 1
    return 0

#find the depth of a binary tree
def depth(root):
    d=0
    while root!=None:
        d=d+1
        root=root.left
    return d
#check for the perfect binary tree
def checkperfectuitll(root,d,level=0):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return d==level+1
    if root.left is None or root.right is None:
        return False
    return (checkperfectuitll(root.left,d,level+1)and checkperfectuitll(root.right,d,level+1))
#final function of calling
def check_perfect_tree(root):
    d=depth(root)
    return checkperfectuitll(root,d)

#check for the tree is a full binary tree or not
def isfullbinary(root):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True
    if root.left is not None and root.right is not None:
        return isfullbinary(root.left) and isfullbinary(root.right)
    return False

#find the sum of the all tree node of a given tree
def sum_tree_all(root):
    sum=0
    if root is None:
        return 0
    return root.key+sum_tree_all(root.left)+sum_tree_all(root.right)
        


#sum of a given parent tree from a given node
def sum_tree_parent(root,sum,x):
    if root is None:
        return
    if (root.left and root.left.key==x) or (root.right and root.right.key==x):
        sum+=root.key

    sum_tree_parent(root.left,sum,x)
    sum_tree_parent(root.right,sum,x)

def sum_tree_parentutill(root,x):
    sum=0
    sum_tree_parent(root,sum,x)
    return sum

#sum of the leaf nodes of given tree
#1:first check for leaf
def check_leaf(root):
    if root is None:
        return False
    if root.left is None and root.right is None:
        return True
    return False
#2:find the sum
def leave_sum(root):
    res=0
    if root is not None:
        if check_leaf(root.left):
            res+=root.left.key
        else:
            res+=leave_sum(root.left)
        res=res+leave_sum(root.right)
    return res
#sum of the all leaf nodes
def leave_right_sum(root):
    sum=0
    if root is None:
        return
    if root.right.left is None and root.right.right is None:
        sum+=root.right.key
    leave_right_sum(root.left)
    leave_right_sum(root.right)
#sum of all node
def sum_of_all(root):
    sum=sumleft=sumright=0
    if root is None:
        return 0
        print("\ntree is empty.")
    if root.left is not None:
        sumleft=sum_of_all(root.left)
    if root.right is not None:
        sumright=sum_of_all(root.right)
    sum=sumleft+sumright+root.key
    return sum
#find the sum of the longest path in tree
def longestpathutill(root):
    if root is None:
        return 0
    maxsum=-9999999
    maxlen=0
    sumoflongestpath(root,0,0,maxlen,maxsum)
    return maxsum
def sumoflongestpath(root,sum,len,maxlenth,maxsum):
    if root is None:
        if maxlenth<len:
            maxlenth=len
            maxsum=sum
        elif len==maxlenth and maxsum<sum:
            maxsum=sum
            return
        sumoflongestpath(root.left,sum+root.key,len+1,maxlenth,maxsum)
        sumoflongestpath(root.right,sum+root.key,len+1,maxlenth,maxsum)

#sum of all the leaf node
def leaf_sum(root):
    global total
    if root is None:
        return
    if root.left is None and root.right is None:
        total=total+root.key
    leaf_sum(root.left)
    leaf_sum(root.right)

#find the lowest common ancester from a given tree
def findpath(root,path,k):
    if root is None:
        return False
    path.append(root.key)
    if root.key==k:
        return True
    if ((root.left!=None and findpath(root.left,path,k)) or (root.right!=None and findpath(root.right,path,k))):
        return True
    path.pop()
    return False
def find_lca(root,n1,n2):
    path1=[]
    path2=[]
    if ((not findpath(root,path1,n1)) or (not findpath(root,path2,n2))):
        return -1
    i=0
    while i<len(path1) and i<len(path2):
        if path1[i]!=path2[i]:
            break
        i+=1
    return path1[i-1]

#find the distance between the two nodes
def distance(root,n1,n2):
    path1=[]
    path2=[]
    if root:
        findpath(root,path1,n1)
        findpath(root,path2,n2)
        #print(path1)
        i=0
        while i<len(path1) and i<len(path2):
            if path1[i]!=path2[i]:
                break
            i+=1
        return len(path1)+len(path2)-2*i
    else:
        return 0
        
    
#print the ancester
def print_ancester(root,data):
    if root is None:
        return False
    if root.key==data:
        return True
    if print_ancester(root.left,data) or  print_ancester(root.right,data):
        print(root.key,end=" ")
        return True
    return False


    









            

key=int(input("Enter the value of the root:"))
t1=node(key)
#t1.insert(10)
#t1.insert(20)
#t1.insert(30)
#t1.insert(40)
#t1.insert(50)
#t1.insert(60)

while True:
    print("\n1:Insert.\t2:Inorder Traversal.\t3:Preorder Traversal.\t4:Levelorder Traversal.")
    print("\n5:Min-value.\t6:Max-value.\t7:Search.\t8:check sum.\t9:Exit.")
    print("\n10:Delete.\t11:Height.\t12:Postorder Traversal.")
    print("\n13:Check the siblings.\t14:Check Cousine.\t15:Check for leaf node same level")
    print("\n16:Check for the check sum.\t17:Depth of a tree.\t18:Check for binary tree.")
    print("\n19:Check full bianry tree.\t20:find the sum.\t21:for sum from a child to parent.")
    print("\n22:Sum of the left leaf nodes.\t23:Sum for all node.\t 24:longest path for sum.")
    print("\n25:Sum of leaf node.\t26: print the least common ancester.\n 27:Find the distance between the nodes.")
    print("\n28:print the ancester.")
    choice=int(input("\nEnter the choice :"))
    if choice==1:
        key1=int(input("\nEnter the value to be insert in the tree: "))
        t1.insert(key1)
    elif choice==2:
        t1.inorder()
    elif choice==3:
        t1.preorder()
    elif choice==4:
        levelorder_traversal(t1)
    elif choice==5:
        print("\nThe minimum value in the tree :",min_val(t1))
    elif choice==6:
        print("\nThe maximum value in the tree :",max_val(t1))
    elif choice==7:
        key1=int(input("\nEnter the value to be search:"))
        if search(t1,key1)==True:
            print("\nNode exist.")
    elif choice==8:
        if check_sum(t1)==1:
            print("\nThe tree satisfy the sum condition.")
        else:
            print("\nThe tree does not satify sum condition.")
    elif choice==9:
        break
    elif choice==10:
        key1=int(input("\nEnter the value to be delete from the tree :"))
        delete_Node(t1,key1)
    elif choice==11:
        print("\nThe height of the tree is :",height(t1))
    elif choice==12:
        t1.postorder()
    elif choice==13:
        c3,c4=map(int,input("\nEnter the two node for check sibling :").split(" "))
        if(is_sibling(t1,node(c3),node(c4)))!=0:
            print("\nthey are siblings.")
        else:
            print("\nThey are not siblings.")
    elif choice==14:
        c3,c4=map(int,input("\nEnter the two node :").split(" "))
        if check_cousine(t1,node(c3),node(c4))==1:
            print("\nThey are Cousine.")
        else:
            print("\nThey are not Cousine.")
    elif choice==15:
        if check(t1)==True:
            print("\nThe leaf nodes are same level.")
        else:
            print("\nThe leaf nodes are same level.")
    elif choice==16:
        if check_sum(t1):
            print("\nThe tree satisfy the check sum.")
        else:
            print("\nThe tree does't satisfy check sum.")
    elif choice==17:
        print("\nThe depth of the tree is: ",depth(t1))
    elif choice==18:
        if check_perfect_tree(t1)==True:
            print("\nThis is perfect binary tree.")
        else:
            print("\nThis is not a perfect binary tree.")
    elif choice==19:
        if isfullbinary(t1)==True:
            print("\nFull binary tree.")
        else:
            print("\nNot a full binary tree!")
    elif choice==20:
        print("\nThe sum for the given tree is :",sum_tree_all(t1))
    elif choice==21:
        c3=int(input("\nEnter the node from where the sum will be calculated :"))
        print("\nThe sum of parent from the given node :",sum_tree_parentutill(t1,c3))
    elif choice==22:
        print("\nThe sum of the left leaf nodes is :",leave_sum(t1))
    elif choice==23:
        print("\nThe sum of the leaf nodes are : ",sum_of_all(t1))
    elif choice==24:
        print("\nThe sum of the longest path is : ",longestpathutill(t1))
    elif choice==25:
        total=0
        leaf_sum(t1)
        print("\nThe sum of the leaf node is :",total)
    elif choice==26:
        n1,n2=map(int,input("\nEnter the two node: ").split(","))
        if find_lca(t1,n1,n2)==-1:
            print("\nNo common ancester.")
        print("\n The common ancester is :",find_lca(t1,n1,n2))
    elif choice==27:
        n1,n2=map(int,input("\nEnter the two nodes :").split(" "))
        if distance(t1,n1,n2)==0:
            print("\nSomething wrong!!")
        else:
            print("\nThe distance between the two nodes is :",distance(t1,n1,n2))
    elif choice==28:
        n1=int(input("\nEnter the target of the tree :"))
        print("\nThe ancester of the given node of the tree is :",print_ancester(t1,n1))
    
    else:
        print("\nWrong choice mate!!!")
        
        
#15 -> 30 -> 35 -> 45 -> 50 -> 60 -> 70 -> 
        








            
