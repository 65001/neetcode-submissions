from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        I_MAX, J_MAX = len(heights), len(heights[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def bounded(middle, upper):
            return 0 <= middle and middle < upper
 
        pacific_source = deque()
        atlantic_source = deque()

        atlantic_reachable = set()
        pacific_reachable = set()

        # (i, j)
        # Pacific Source (*, 0) and (0, *)
        # Atlantic Source (*, J_MAX - 1) and (I_MAX - 1, *)
        # Determine the Sources
        for i in range(I_MAX):
            for j in range(J_MAX):
                if j == 0 or i == 0:
                    pacific_source.append( (i, j) )
                    pacific_reachable.add( (i, j) )
                if j == J_MAX - 1 or i == I_MAX - 1:
                    atlantic_source.append( (i, j) )
                    atlantic_reachable.add( (i, j) )
        
        # Determine cells that are reachable from the Pacific Ocean
        while len(pacific_source) > 0:
            x, y = pacific_source.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if not bounded(nx, I_MAX) or not bounded(ny, J_MAX):
                    continue
                if heights[nx][ny] < heights[x][y]:
                    continue
                if (nx, ny) in pacific_reachable:
                    continue
                pacific_source.append((nx, ny))
                pacific_reachable.add((nx, ny))

        # Determine cells that are reachable from the Atl. Ocean
        while len(atlantic_source) > 0:
            x, y = atlantic_source.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if not bounded(nx, I_MAX) or not bounded(ny, J_MAX):
                    continue
                if heights[nx][ny] < heights[x][y]:
                    continue
                if (nx, ny) in atlantic_reachable:
                    continue
                atlantic_source.append((nx, ny))
                atlantic_reachable.add((nx, ny))
        # Determine cells that are reachable from both oceans
        return list(atlantic_reachable.intersection(pacific_reachable))