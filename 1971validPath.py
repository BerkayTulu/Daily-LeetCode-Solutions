# There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.
# You want to determine if there is a valid path that exists from vertex source to vertex destination.
# Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

# Example 1:
# Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
# Output: true
# Explanation: There are two paths from vertex 0 to vertex 2:
# - 0 → 1 → 2
# - 0 → 2

# Example 2:
# Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
# Output: false
# Explanation: There is no path from vertex 0 to vertex 5.
 
class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        graph = {}
        for u, v in edges:
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        def dfs(node):
            if node == destination:
                return True
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
            return False
        return dfs(source)
    
#test cases
s = Solution()
print(s.validPath(3, [[0,1],[1,2],[2,0]], 0, 2)) #True
print(s.validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5)) #False
print(s.validPath(5, [[0,1],[1,2],[2,3],[3,4]], 0, 4)) #True