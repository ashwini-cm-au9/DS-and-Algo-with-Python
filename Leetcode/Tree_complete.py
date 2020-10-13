class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class Read:
    def preOrder(self, tree): # pre order traversal
        if tree is None:
            return
        print(tree.val,end=" ")
        self.read_val(tree.left)
        self.read_val(tree.right)

    def inOrder(self, tree): # in order traversal
        if tree is None:
            return
        self.read_val(tree.left)
        print(tree.val,end=" ")
        self.read_val(tree.right)
    
    def postOrder(self, tree): # post order traversal
        if tree is None:
            return
        self.read_val(tree.left)
        self.read_val(tree.right)
        print(tree.val,end=" ")

    def level(self,tree):  #level order traversal using 
        if tree is None:
            return 
        qq=[]
        qq.append(tree)
        res=[]
        while(len(qq)>0):
            j=[]
            for i in range(len(qq)):
                x=qq.pop(0)
                j.append(x.val)

                if x.left is not None:
                    qq.append(x.left)
                if x.right is not None:
                    qq.append(x.right)
            res.append(j)
        return res

    def path(self,tree,cur,path): # paths in a tree
        if tree is None:
            return
        if tree.left is None and tree.right is None:
            cur.append(tree.val)
            path.append(cur[:])
            cur.pop()
        cur.append(tree.val)
        self.path(tree.left,cur,path)
        self.path(tree.right,cur,path)
        cur.pop()

    def pathSum(self,tree,cur,path_sum): # path sum
        if tree is None:
            return

        if tree.left is None and tree.right is None:
            cur.append(tree.val)
            path_sum.append(sum(cur[:]))
            cur.pop()

        cur.append(tree.val)
        self.pathSum(tree.left,cur,path_sum)
        self.pathSum(tree.right,cur,path_sum)
        cur.pop()


if __name__ == "__main__":
    tree=TreeNode(3)
    tree.left=TreeNode(9)
    tree.right=TreeNode(20)
    tree.right.left=TreeNode(15)
    tree.right.right=TreeNode(7)
    r=Read()
    # r.read_val(tree)
    # print(r.level(tree))
    cur=[]
    path_sum=[]
    r.pathSum(tree,cur,path_sum)
    print(path_sum)
    