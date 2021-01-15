class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if '0000' in deadends: return -1
        stack = deque(['0000'])
        visited = set(['0000'])
        res = 0
        while stack:
            n = len(stack)
            for i in range(n):
                current = stack.popleft()
                #print(current)
                if current == target: return res
                if current in deadends: continue
                for k in range(4):
                    s1 = current[:k] + str((int(current[k]) + 1)%10) + current[k+1:]
                    s2 = current[:k] + str((int(current[k]) - 1)%10) + current[k+1:]
                    if s1 not in visited and s1 not in deadends:
                        visited.add(s1)
                        stack.append(s1)
                    if s2 not in visited and s1 not in deadends:
                        visited.add(s2)
                        stack.append(s2)
            res += 1
        return -1