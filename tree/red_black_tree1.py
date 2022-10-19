#implementing the red black tree
import random
class RbtNode:
    def __init__(self,data):
        self.data=data
        self.parent=None
        self.left=None
        self.right=None
        self.red=False

#implementing the red black class
class RbTree:
    def __init__(self):
        self.nil=RbtNode(0)
        self.nil.parent=None
        self.nil.left=None
        self.nil.right=None
        self.nil.red=False
        self.root=None

    
























            
