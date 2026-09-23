from collections import deque 

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        I_MAX, J_MAX = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def bounded(middle, upper):
            return 0 <= middle and middle < upper
        
        # Scan the entire grid for the tresaure chests!
        queue = deque()
        for i in range(I_MAX):
            for j in range(J_MAX):
                if grid[i][j] == 0:
                    queue.append( (0, i, j) )
        
        while len(queue) > 0:
            distance, x, y = queue.popleft()
            # Distance, x, y 
            for dx, dy in directions:
                n_distance, nx, ny = distance + 1, x + dx, y + dy
                if not bounded(nx, I_MAX) or not bounded(ny, J_MAX):
                    continue
                # We are not allowed to traverse water
                if grid[nx][ny] == -1:
                    continue
                # We do not want to set the distance, if the current grid distance is already smaller than this one...
                if grid[nx][ny] != INF:
                    continue
                # Preemptively mark the grid
                grid[nx][ny] = n_distance
                queue.append((n_distance, nx, ny))