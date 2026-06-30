class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]  # monotonic decreasing stack
        res = [0 for _ in temperatures]

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                prev = stack.pop(-1)
                res[prev] = i - prev
            stack.append(i)
        
        # res[-1] already initialised to 0
        return res
