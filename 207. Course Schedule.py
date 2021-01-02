class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for prerequisite in prerequisites:
            graph[prerequisite[0]].append(prerequisite[1])
        visited = [0]*numCourses
        def dfs(course):
            if visited[course] == 1: return True
            if visited[course] == 2: return False
            
            visited[course] = 1
            for prereq in graph[course]:
                if dfs(prereq): return True
            visited[course] = 2
            return False
        for course in list(graph.keys()):
            if dfs(course): return False
        return True
            