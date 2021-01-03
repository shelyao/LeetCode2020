class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if n == m: return n
        groups = [(1, n)]
        for i in range(n-1, -1, -1):
            temp = []
            for l, r in groups:
                if l <= arr[i] <= r:
                    if arr[i] - l == m or r - arr[i] == m: return i
                    if arr[i] - l > m:
                        temp.append((l, arr[i] - 1))
                    if r - arr[i] > m:
                        temp.append((arr[i]+1, r))
                elif r - l >= m:
                    temp.append((l, r))
            groups = temp
        return -1