# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def bfs(root, result):
            if root is None:
                result.append("null")
                return
            result.append(root.val)
            bfs(root.left, result)
            bfs(root.right, result)
            return result
        result1 = []
        result2 = []
        bfs(p, result1)
        bfs(q, result2)

        return result1 == result2

        

