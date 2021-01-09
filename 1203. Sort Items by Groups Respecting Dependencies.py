class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        groupSet = set(group)
        validGroup = [i for i in range(max(m, n), -1, -1) if i not in groupSet]
        for idx, grp in enumerate(group):
            if grp == -1: group[idx] = validGroup.pop()
        itemGraph, groupGraph = defaultdict(list), defaultdict(list)
        itemIndegree, groupIndegree = [0]*n, [0]*n
        for idx, items in enumerate(beforeItems):
            for item in items:
                itemGraph[item].append(idx)
                itemIndegree[idx] += 1
                if group[idx] != group[item]:
                    groupGraph[group[item]].append(group[idx])
                    groupIndegree[group[idx]] += 1
        #print(itemGraph, groupGraph)
        def topoSort(graph, indegree):
            stack = deque([i for i in range(len(indegree)) if indegree[i] == 0])
            res = []
            while stack:
                curr = stack.popleft()
                res.append(curr)
                for neighbor in graph[curr]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        stack.append(neighbor)
            if len(res) == len(graph): return res
            return []
        
        itemOrder = topoSort(itemGraph, itemIndegree)
        groupOrder = topoSort(groupGraph, groupIndegree)
        #print(itemOrder, groupOrder)
        if itemOrder == [] or groupOrder == []: return []
        itemsMap, res = defaultdict(list), []
        for item in itemOrder:
            itemsMap[group[item]].append(item)
        for grp in groupOrder:
            res.extend(itemsMap[grp])
        return res
            