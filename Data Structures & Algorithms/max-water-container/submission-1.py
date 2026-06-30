class Solution:
    def maxArea(self, heights: List[int]) -> int:
        j = len(heights) - 1
        if j < 1:
            return 0

        def calc_area(i, j):
            return abs(i-j) * min(heights[i], heights[j])
        
        i = 0
        area = calc_area(i, j)

        while i < j:
            if heights[i] < heights[j]:
                i += 1
            elif heights[j] < heights[i]:
                j -= 1
            else:
                # bars are equal height making the choice arbitrary
                i += 1
        
            area = max(area, calc_area(i, j))

        return area