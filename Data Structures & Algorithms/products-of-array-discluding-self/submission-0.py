class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Naive solution.
        length = len(nums)
        res = [1] * length
        for i in range(length):
            for j, num in enumerate(nums):
                if j != i:
                    res[i] *= num
        return res