class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        graph, indegree = defaultdict(list), defaultdict(int)
        for seq in seqs:
            if len(seq) == 1:
                graph[seq[0]]
                indegree[seq[0]]
            for i in range(len(seq) - 1):
                graph[seq[i]].append(seq[i+1])
                indegree[seq[i + 1]] += 1
        
        stack = [nd for nd in graph.keys() if indegree[nd] == 0]
        #print(graph, indegree, stack)
        nums = []
        while stack:
            if len(stack) > 1: return False
            curr = stack.pop()
            nums.append(curr)
            for nd in graph[curr]:
                indegree[nd] -= 1
                if indegree[nd] == 0:
                    stack.append(nd)
        if sum(indegree.values()) > 0: return False
        #print(nums)
        return org == nums