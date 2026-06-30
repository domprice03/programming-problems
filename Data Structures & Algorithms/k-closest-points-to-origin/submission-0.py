import heapq
from math import sqrt

class Solution:
    class Point:
        def __init__(self, point: list[int]):
            self._point = point
            self._dist = sqrt((point[0]**2 + point[1]**2))

        @property
        def point(self) -> list[int]:
            return self._point

        @property
        def dist(self) -> float:
            return self._dist
        
        def __lt__(self, other) -> bool:
            return self.dist < other.dist
        
        def __eq__(self, other) -> bool:
            return self.dist == other.dist

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = [self.Point(point) for point in points]
        heapq.heapify(min_heap)
        return [heapq.heappop(min_heap).point for _ in range(k)]
            