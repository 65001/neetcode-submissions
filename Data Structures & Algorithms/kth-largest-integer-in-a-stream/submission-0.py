import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.largest = k
        heapq.heapify(nums)
        self.nums = nums
        while len(self.nums) > self.largest:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        while len(self.nums) > self.largest:
            heapq.heappop(self.nums)
        return self.nums[0]
        
