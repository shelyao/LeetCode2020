class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        stack = deque([(0, 0)])
        visited = set()
        visited.add(0)
        res = 0
        maxVal = max([x] + forbidden) + a + b
        while stack:
            n = len(stack)
            for i in range(n):
                prev, curr = stack.popleft()
                #print(curr)
                if curr == x: return res
                if prev < curr:
                    if curr - b >= 0 and curr - b not in visited and curr - b not in forbidden:
                        stack.append((curr, curr - b))
                        visited.add(curr - b)
                if curr + a not in visited and curr + a <= maxVal and curr + a not in forbidden:
                    stack.append((curr, curr + a))
                    visited.add(curr + a)
            #print(stack)
            res += 1
        return -1