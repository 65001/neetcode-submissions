import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Make all the numbers negative so that heapq becomes a max heap!
        for i in range(len(stones)):
            stones[i] = -1 * stones[i]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones) * -1 
            y = heapq.heappop(stones) * -1
            if x == y:
                continue
            elif x < y:
                y = y - x
                heapq.heappush(stones, y * -1)
            else:
                x = x - y
                heapq.heappush(stones, x * -1)
        if len(stones) == 0:
            return 0
        return stones[0] * -1
        