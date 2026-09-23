import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for coordinate in points:
            x,y = coordinate[0], coordinate[1]
            distance = math.sqrt(x * x + y * y)
            heapq.heappush(heap, (distance, [x, y]))
        results = []
        while len(results) < k:
            entry = heapq.heappop(heap)
            results.append( entry[1] )
        return results
        