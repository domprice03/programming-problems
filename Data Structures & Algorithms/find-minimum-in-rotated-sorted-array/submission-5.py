class Solution:
    def findMin(self, nums: List[int]) -> int:
        length = len(nums)
        left = 0
        mid = 0
        right = length - 1

        while left < right:
            if nums[left] < nums[right]:
                return nums[left]

            mid = (left + right) // 2
            
            if nums[left] < nums[mid]:
            # if nums[right] > nums[mid]:
                left = mid + 1
            else:
                right = mid
        
        return nums[(mid + 1) % length]
