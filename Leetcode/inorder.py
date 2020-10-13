class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class Read:
    def read_val(self, tree):
        if tree is None:
            return
        print(tree.val,end=" ")
        self.read_val(tree.left)
        self.read_val(tree.right)
if __name__ == "__main__":
    tree=TreeNode(3)
    tree.left=TreeNode(4)
    tree.right=TreeNode(5)
    tree.left.left=TreeNode(6)
    tree.left.right=TreeNode(7)
    r=Read()
    r.read_val(tree)