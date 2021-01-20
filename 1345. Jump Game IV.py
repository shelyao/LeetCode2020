class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1: return 0
        if arr[0] == arr[-1]: return 1
        n = len(arr)
        graph = defaultdict(list)
        res = 0
        for idx, num in enumerate(arr):
            graph[num].append(idx)
        stack = deque([(0, arr[0])])
        visited = set([0])
        while stack:
            k = len(stack)
            for i in range(k):
                node, val = stack.popleft()
                if node == n - 1: return res
                if node - 1 >= 0 and node - 1 not in visited:
                    visited.add(node - 1)
                    stack.append((node - 1, arr[node - 1]))
                if node + 1 < n and node + 1 not in visited:
                    visited.add(node + 1)
                    stack.append((node + 1, arr[node + 1]))
                for next_idx in graph[val]:
                    if next_idx not in visited:
                        visited.add(next_idx)
                        stack.append((next_idx, arr[next_idx]))
                graph[arr[node]].clear()
            res += 1
        return res