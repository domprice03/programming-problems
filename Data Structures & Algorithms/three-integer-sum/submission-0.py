class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for p3, num3 in enumerate(nums):
            # Skip duplicates for p3
            if p3 >= 1 and num3 == nums[p3-1]:
                continue
            p1 = p3 + 1
            p2 = len(nums) - 1
            while p1 < p2:
                num1, num2 = nums[p1], nums[p2]
                num_sum = num3 + num1 + num2
                if num_sum < 0:
                    p1 += 1
                elif num_sum > 0:
                    p2 -= 1
                else:
                    triplets.append([num1, num2, num3])
                    # Use sorted property to skip duplicates for p1 and p2
                    while num1 == nums[p1] and p1 < p2:
                        p1 += 1
                    while num2 == nums[p2] and p1 < p2:
                        p2 -= 1
        return triplets