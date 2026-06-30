from heapq import heapify, heappush, heappop, heappushpop

class KthLargest:

    def __init__(self, k: int, nums: List[int]) -> None:
        # Stores kth largest element and all those larger
        self._min_heap = nums
        heapify(self._min_heap)
        self._k = k
        for _ in range(len(nums) - k):
            heappop(self._min_heap)
        
    def add(self, val: int) -> int:
        if len(self._min_heap) == self._k:
            if val >= self._min_heap[0]:
                heappushpop(self._min_heap, val)
        else:
            heappush(self._min_heap, val)
            
        return self._min_heap[0]
                
