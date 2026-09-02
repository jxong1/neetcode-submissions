# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        tree = []
        self.BFS(root, tree, 0)
        return tree

    def BFS(self, root, lst, level):
        if not root:
            return
        if len(lst) <= level:
            lst.append([])
        lst[level].append(root.val)

        self.BFS(root.left, lst, level + 1)
        self.BFS(root.right, lst, level + 1)