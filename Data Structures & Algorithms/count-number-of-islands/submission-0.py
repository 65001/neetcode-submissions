class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Helpful constants
        I_MAX, J_MAX = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def bounded(lower, middle, upper):
            # Gurantee that we are accessing an entry that inside the array bounds
            return lower <= middle and middle < upper

        def markIsland(i: int, j: int):
            # Input: Grid, and i, j
            # Sink the island
            if not bounded(0, i, I_MAX) or not bounded(0, j, J_MAX):
                return
            if grid[i][j] == "0":
                return

            grid[i][j] = "0" # Sink the island, by converting the island to water
            for deltaX, deltaY in directions:
                markIsland(i + deltaX, j + deltaY)
        
        count = 0
        for i in range(I_MAX):
            for j in range(J_MAX):
                if grid[i][j] == "1":
                    markIsland(i, j)
                    count = count + 1
        return count