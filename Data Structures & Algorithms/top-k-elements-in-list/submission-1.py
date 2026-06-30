from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums)+1)]
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1

        for num, count in counts.items():
            buckets[count].append(num)
        
        for bucket in buckets:
            sorted(bucket)

        # Return the top k non-empty lists in buckets, by flattening.
        flattened_buckets = [num for bucket in buckets for num in bucket]
        return flattened_buckets[-k:]