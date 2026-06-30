class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed_nums = [(i, num) for i, num in enumerate(nums)]
        sorted_nums = sorted(indexed_nums, key = lambda x: (x[1], x[0]))
        nums_len = len(nums)
        i_0 = 0
        i_1 = nums_len - 1

        while i_0 < i_1 and i_1 < nums_len:
            num_sum = sorted_nums[i_0][1] + sorted_nums[i_1][1]
            if num_sum == target:
                idx_1 = sorted_nums[i_0][0]
                idx_2 = sorted_nums[i_1][0]
                return [min(idx_1, idx_2), max(idx_1, idx_2)]
            elif num_sum < target:
                i_0 += 1
            else:
                i_1 -= 1
