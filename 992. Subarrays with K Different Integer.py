class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        if K == 0: return 0
        n = len(A)
        l1 = l2 = res = 0
        charMap1 = defaultdict(int)
        charMap2 = defaultdict(int)
        for right in range(n):
            charMap1[A[right]] += 1
            charMap2[A[right]] += 1
            while len(charMap1) > K:
                charMap1[A[l1]] -= 1
                if charMap1[A[l1]] == 0: del charMap1[A[l1]]
                l1 += 1
            while len(charMap2) >= K:
                charMap2[A[l2]] -= 1
                if charMap2[A[l2]] == 0: del charMap2[A[l2]]
                l2 += 1
            res += l2-l1
        return res