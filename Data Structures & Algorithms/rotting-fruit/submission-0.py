from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        I_MAX, J_MAX = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        def bounded(middle, upper):
            return 0 <= middle and middle < upper

        # Identify all of the fresh fruit in a set
        # Identify all of the rotten fruit as a deque

        fresh_fruit = set()
        queue = deque()

        for i in range(I_MAX):
            for j in range(J_MAX):
                if grid[i][j] == 1:
                    fresh_fruit.add((i, j))
                elif grid[i][j] == 2:
                    queue.append( (0, i, j))
        
        max_distance = 0
        while len(queue) > 0:
            distance, x, y = queue.popleft()
            max_distance = max(max_distance, distance)
            for dx, dy in directions:
                n_distance, nx, ny = distance + 1, x + dx, y + dy
                # Do a bounds check!
                if not bounded(nx, I_MAX) or not bounded(ny, J_MAX):
                    continue
                # Ensure we are only checking fresh fruit
                if grid[nx][ny] != 1:
                    continue
                fresh_fruit.remove((nx, ny))
                grid[nx][ny] = 2
                queue.append( (n_distance, nx, ny) )

        if len(fresh_fruit) > 0:
            return -1

        return max_distance

