#lca recursive 
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def lca(root,n1,n2):
    if root is None:
        return None
    if root.data == n1 or root.data == n2:
        return root
    l_ca = lca(root.left,n1,n2)
    r_ca = lca(root.right,n1,n2)

    if l_ca and r_ca:
        return root

    return l_ca if l_ca!=None else r_ca


root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(6)
root.right.right = node(7)

print("LCA(4, 5) = %d" % (lca(root, 4, 5).data))
print("LCA(4, 6) = %d" % (lca(root, 4, 6).data))
print("LCA(3, 4) = %d" % (lca(root, 3, 4).data))
print("LCA(2, 4) = %d" % (lca(root, 2, 4).data))
print("LCA(5, 6) = %d" % (lca(root, 5, 6).data))
