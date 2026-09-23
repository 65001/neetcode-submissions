from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        I_MAX , J_MAX = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def bounded(lower, middle, upper):
            return lower <= middle and middle < upper

        def areaOfIsland(i, j) -> int:
            area = 0
            q = deque()
            q.append((i, j))
            grid[i][j] = 0

            while len(q) > 0:
                x, y = q.popleft()
                area = area + 1

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if not bounded(0, nx, I_MAX) or not bounded(0, ny , J_MAX):
                        continue
                    if grid[nx][ny] == 0:
                        continue
                    q.append((nx, ny))
                    grid[nx][ny] = 0
            
            return area

        
        maximum = 0
        for i in range(I_MAX):
            for j in range(J_MAX):
                if grid[i][j] == 1:
                    area = areaOfIsland(i, j)
                    maximum = max(maximum, area)
        return maximum