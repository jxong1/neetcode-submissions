# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if root.val == subRoot.val:
            if (self.isSubtree(root.left, subRoot.left) and self.isSubtree(root.right, subRoot.right)):
                if (root.left and root.right):
                    return root.left.val == subRoot.left.val and root.right.val == subRoot.right.val
                else:
                    return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)