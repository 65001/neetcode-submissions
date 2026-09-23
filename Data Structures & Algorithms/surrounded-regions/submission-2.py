from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:

        def bounded(middle, upper):
            return 0 <= middle and middle < upper
        # Goal
        # From the edges, find all regions that are 'O' reachable
        # Go through the grid, and tag all entries not

        I_MAX, J_MAX = len(board), len(board[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        o_reachable = set()
        queue = deque()

        # Find all of the 'O' islands that are on the edge
        for i in range(I_MAX):
            for j in range(J_MAX):
                xEdge = i == 0 or i == I_MAX - 1
                yEdge = j == 0 or j == J_MAX - 1
                isO = board[i][j] == 'O'
                if not isO:
                    continue
                if xEdge or yEdge:
                    queue.append((i, j))
                    o_reachable.add((i, j))

        while len(queue) > 0:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if not bounded(nx, I_MAX) or not bounded(ny, J_MAX):
                    continue
                if board[nx][ny] != 'O':
                    continue
                if (nx, ny) in o_reachable:
                    continue
                queue.append((nx, ny))
                o_reachable.add((nx, ny))
        
        for i in range(I_MAX):
            for j in range(J_MAX):
                # The entry must be an O and (i, j) cannot be in o_reachable
                if board[i][j] == 'O' and not (i, j) in o_reachable:
                    board[i][j] = 'X'

