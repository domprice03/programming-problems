class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts: dict[int, int] = defaultdict(int)

        for num in nums:
            counts[num] += 1

        key_vals = [(num, count) for num, count in counts.items()]
        key_vals.sort(key = lambda x: x[1])

        return [x[0] for x in key_vals[-k:]]