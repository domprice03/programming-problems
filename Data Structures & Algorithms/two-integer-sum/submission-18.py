class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            diff = target - num
        
            if num in hashmap:
                j = hashmap[num]
                if i != j:
                    return [min(i, j), max(i, j)]

            hashmap[diff] = i