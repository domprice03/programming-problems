class Solution:
    def climbStairs(self, n: int) -> int: 
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp_table = [1, 2]

        for i in range(n-2):
            dp_table.append(dp_table[-1]+dp_table[-2])

        return dp_table[-1]
