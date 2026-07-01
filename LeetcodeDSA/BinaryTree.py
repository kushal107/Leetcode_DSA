class TreeNode:
    def __init__(self,val, left, right):
        self.val = val
        self.left = left
        self.right = right

Three = TreeNode(3,None,None)
Two = TreeNode(2,None, None)    
One = TreeNode(1,Two,Three)

print(f" {One.val}")
print(One.left.val, One.right.val)
