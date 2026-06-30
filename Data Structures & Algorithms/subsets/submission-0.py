class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        result: list[list[int]] = []

        def backtrack(i: int, subset: list[int]) -> None:
            if i == length:
                result.append(subset.copy())
                return

            subset.append(nums[i])
            backtrack(i+1, subset)

            subset.pop(-1)
            backtrack(i+1, subset)

        backtrack(0, [])
        return result