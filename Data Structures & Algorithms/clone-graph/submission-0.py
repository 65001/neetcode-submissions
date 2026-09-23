"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        visited = {}
        def dfs(node: Optional['Node']) -> Optional['Node']:
            if not node: 
                return None
            if node in visited:
                return visited[node]

            clone = Node(node.val, [])
            visited[node] = clone

            for child in node.neighbors:
                clone.neighbors.append(dfs(child))

            return clone
        return dfs(node)



