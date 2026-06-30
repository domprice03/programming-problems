# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 0)]
        max_depth = 0

        while stack:
            curr, depth = stack.pop()

            if curr is None:
                max_depth = max(max_depth, depth)
            else:
                stack.append((curr.left, depth + 1))
                stack.append((curr.right, depth + 1))

        return max_depth
