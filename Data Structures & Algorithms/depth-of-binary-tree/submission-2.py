# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # stack = [(root, 0)]
        # max_depth = 0

        # while stack:
        #     curr, depth = stack.pop()

        #     if curr is None:
        #         max_depth = max(max_depth, depth)
        #     else:
        #         stack.append((curr.left, depth + 1))
        #         stack.append((curr.right, depth + 1))

        # return max_depth
        if not root:
            return 0

        q = deque()
        q.append(root)
        depth = 0

        while q:
            for _ in range(len(q)):
                curr = q.popleft()

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            depth += 1

        return depth
