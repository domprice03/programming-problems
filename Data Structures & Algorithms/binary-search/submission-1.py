class Solution:
    def search(self, nums: List[int], target: int) -> int:
        j = len(nums) - 1
        i = 0
        while i <= j:
            mid = (i+j) // 2
            num = nums[mid]
            if num == target:
                return mid
            elif num > target:
                j = mid - 1
            else:
                i = mid + 1
        return -1