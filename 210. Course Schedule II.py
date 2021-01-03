class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if prerequisites == []: return [i for i in range(numCourses)]
        graph = defaultdict(list)
        for p in prerequisites:
            graph[p[0]].append(p[1])
        visited = [0]*numCourses
        ordered_crs = []
        ##check if there is any circle in the graph
        def dfs(current):
            if visited[current] == 1: return True
            if visited[current] == 2: return False
            visited[current] = 1
            for p in graph[current]:
                if dfs(p): return True
            visited[current] = 2
            ordered_crs.append(current)
            return False
        
        for crs in range(numCourses):
            if dfs(crs): return []
        return ordered_crs