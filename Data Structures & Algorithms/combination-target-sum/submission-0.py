class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combos = []
        stopping_i = len(nums) - 1

        # TODO: stop adding duplicates.
        def backtrack(subset: list[int], i: int) -> None:
            subset_sum = sum(subset)
            if subset_sum == target:
                combos.append(subset)
                return
            elif subset_sum > target:
                return

            backtrack(subset+[nums[i]], i)

            if i >= stopping_i:
                return

            backtrack(subset, i+1)

        backtrack([], 0)
        return combos