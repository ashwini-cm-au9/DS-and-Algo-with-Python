class Node:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None
def insert(root,node):
    if root is None:
        root=node
    else:
        if root.val<node.val:
            if root.right is None:
                root.right=node
            else:
                insert(root.right,node)
        else:
            if root.left is None:
                root.left=node
            else:
                insert(root.left,node)
            
def pri(r):
    if r is None:
        return
    print(r.val,end=" ")
    pri(r.right)
    pri(r.left)
    

r=Node(30)
insert(r,Node(15))
insert(r,Node(60))
pri(r)
