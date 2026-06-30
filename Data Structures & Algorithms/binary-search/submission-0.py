class Solution:
    def search(self, nums: List[int], target: int) -> int:
        j = len(nums) - 1
        i = 0
        mid = j // 2
        num = nums[mid]
        while num != target:
            if num > target:
                j = mid
            elif num < target:
                i = mid
            if j - i <= 1:
                if nums[j] == target:
                    return j
                elif nums[i] == target:
                    return i
                else:
                    return -1
            mid = (i + j) // 2
            num = nums[mid]
        return mid