from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        # Heap is a Min Heap which tracks the lowest to max frequencies
        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            # If we exceed the k elements, we can drop a low frequency number
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        