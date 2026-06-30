class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [1] * length
        for i in range(1, length, 1):
            res[i] *= res[i-1] * nums[i-1]
        running_product = 1
        for i in range(length-2, -1, -1):
            running_product *= nums[i+1]
            res[i] *= running_product
        return res