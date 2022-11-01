#basic tree implementation



class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    #inorder traversal
    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.data,'>>',end=" ")
        if self.right is not None:
            self.right.inorder()


    #preorder traversal
    def preorder(self):
        print(self.data,'>>',end=" ")
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()


    #postorder traversal
    def postorder(self):
        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        print(self.data,'>>',end=" ")
    
#inserting the data in Tree
    def insert(self,data):
        if self.data < data:
            if self.right is None:
                self.right = node(data)
            else:
                self.right.insert(data)
        elif self.data > data :
            if self.left is None:
                self.left = node(data)
            else:
                self.left.insert(data)
    
    #search the data in tree
    def search(self,data):
        if self.data == data :
            return True
        elif self.data < data :
            return self.right.search(data)
        elif self.data > data:
            return self.left.search(data)
        else:
            return False
#delete the node in the tree
#Algotim is 
def minvalue(root):
    curr = root
    while curr.left is not None:
        curr = curr.left
    return curr

#main delete function
def delete(root,key):
    #best case
    if root is None:
        return root
    if root.data < key:
        root.right = delete(root.right,key)
    elif root.data > key :
        root.left = delete(root.left,key)
    else:
        #node with only children
        if root.left is None:
            temp = root.right
            root= None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        else:
            temp = minvalue(root.right)
            root.key = temp.key
            root.right = delete(root.right,temp.key)
        return root


#height of tree
def height(root):
    if root is None:
        return 0
    lmax = height(root.left)
    rmax = height(root.right)
    return max(lmax,rmax)+1
#level order traversal of the binary tree
#alogorithm is
# find the height
#2. iter form the height
#3.   if root is None
#         return
#4.   if root level is 1
         # print data
#5.   level is greater than 1
#       then recursive function
def curr_level(root,level):
    if root is None:
        return 
    if level == 1:
        print(root.data,end = " ")
    elif level > 1:
        curr_level(root.left,level-1)
        curr_level(root.right,level-1)
#main levelorder
def levelorder(root):
    h = height(root)
    for i in range(1,h+1):
        curr_level(root,i)

#another try of levelorder traversal using Queue
def levelorder_Queue(root):
    if root is None:
        return
    Q = []
    Q.append(root)
    while len(Q) > 0:
        temp = Q.pop()
        print(temp.data," >> ",end =" ")
        if temp.left is not None:
            Q.append(temp.left)
        if temp.right is not None:
            Q.append(temp.right)
#breadth first search of the tree 
def breadth_first_search(root):
    if root is None:
        return
    Q = []
    Q.append(root)
    while len(Q)!=0:
        temp = Q.pop(0)
        print(temp.data,' >> ',end = " ")
        if temp.left is not None:
            Q.append(temp.left)
        if temp.right is not None:
            Q.append(temp.right)

#size of the binary tree
def treeSize(root):
    if root is None:
        return 0
    else:
        Q = []
        Q.append(root)
        clock = 0
        while len(Q)!=0:
            temp = Q.pop(0)
            clock+=1
            if temp.left is not None:
                Q.append(temp.left)
            if temp.right is not None:
                Q.append(temp.right)
        return clock

#Basic operation in Binary Tree data structer:
#1. Inserting an element.
#2. Removing an element.
#3. Searching for an element.
#3. Traversing an element. There are three types of traversals in a binary tree which will be discussed ahead.


#auxaliary operation in Binary Tree Data structer:
#1. Finding the height of the tree
#2. Find the level of the tree
#3. Finding the size of the entire tree.


     

#testing tree data Structer
#root_data = int(input("enter the root data :"))
t1= node(50)
arr = [40 ,20,30,10,90,70,60]
while True:
    print("\n")
    print("0: exit the loop.")
  #  print("1: insert data.")
    print("2: inorder data.")
    print("3: preorder data.")
    print("4: postorder data.")
    print("5: search data.")
    print("6: delete")
    print("7: height.")
    print("8: levelorder.")
    print("10: levelorder Queue.")
    print("9: tree size.")
    choice = int(input("enter choice : "))
    for i in range(len(arr)):
        t1.insert(arr[i])
   # if choice==1:
    #    data = int(input("enter the data :"))
     #   t1.insert(data)
    if choice == 2:
        print("printing the inorder tree .....")
        t1.inorder()
    elif choice == 3:
        print("printing the preorder tree ......")
        t1.preorder()
    elif choice == 4 :
        print("printing the postorder tree ......")
        t1.postorder()
    elif choice == 0:
        exit(0)
    elif choice == 5:
        data = int(input("enter data to be search :"))
        if t1.search(data) == True:
            print("{0} present in the tree.".format(data))
        else:
            print("{0} not present in the tree.".format(data))
    elif choice == 6: 
        data = int(input("enter data to delete:"))
        delete(t1,data)

    elif choice == 7:
        print("The height of the tree is : ",height(t1))
    
    elif choice == 8:
        print("\nThe levelorder is :")
        levelorder(t1)

    elif choice == 9:
        print("The size of the tree is :",treeSize(t1))
    elif choice == 10:
        print("The level order traversal using Queue is :")
        levelorder_Queue(t1)
    else:
        choice = int(input("enter choice"))

