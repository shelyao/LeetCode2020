class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        stack = [start]
        visited = set([start])
        n = len(arr)
        while stack:
            idx = stack.pop()
            if arr[idx] == 0: return True
            if idx + arr[idx] < n and idx + arr[idx] not in visited:
                visited.add(idx + arr[idx])
                stack.append(idx + arr[idx])
            if idx - arr[idx] >= 0 and idx - arr[idx] not in visited:
                visited.add(idx - arr[idx])
                stack.append(idx - arr[idx])
        return False