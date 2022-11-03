#this is the recursive function for the lowest common ancester
class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
#lca function recursive
def lca_recursive(root,n1,n2):
    if root == None :
        return None
    if root.data == n1 or root.data == n2:
        return root
    left_lca = lca_recursive(root.left,n1,n2)
    right_lca = lca_recursive(root.right,n1,n2)
    # if booth returns non null value then the root returns the root value
    if left_lca and right_lca:
        return root
    return left_lca if left_lca is not None else right_lca

root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(6)
root.right.right = node(7)
print("LCA(4, 5) = ", lca_recursive(root, 4, 5).data)
print("LCA(4, 6) = ", lca_recursive(root, 4, 6).data)
print("LCA(3, 4) = ", lca_recursive(root, 3, 4).data)
print("LCA(2, 4) = ", lca_recursive(root, 2, 4).data)