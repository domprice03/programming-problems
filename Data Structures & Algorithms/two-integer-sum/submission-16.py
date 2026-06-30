class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            diff = target - num
            hashmap[diff] = i
        
        for i, num in enumerate(nums):
            if num in hashmap:
                j = hashmap[num]
                if i != j:
                    return [min(i, j), max(i, j)]
