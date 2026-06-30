class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers) - 1
        while p1 < p2:
            num_sum = numbers[p1] + numbers[p2]
            if num_sum == target:
                return [p1+1, p2+1]
            if num_sum < target:
                p1 += 1
            elif num_sum > target:
                p2 -= 1