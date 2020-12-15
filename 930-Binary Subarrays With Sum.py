class Solution:
    # Prefix Sum
    def numSubarraysWithSum0(self, A: List[int], S: int) -> int:
        res, prefixSum = 0, [0]
        count = defaultdict(int)
        for num in A:
            prefixSum.append(prefixSum[-1] + num)
        for s in prefixSum:
            res += count[s]
            count[s+S] += 1
        return res
    
    # 3 pointers: for each j: low, high
    # res += high - low + 1
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        lowIdx = highIdx = 0
        lowSum = highSum = 0
        N, res =len(A), 0
        for i, num in enumerate(A):
            lowSum += num
            while lowIdx < i and lowSum > S:
                lowSum -= A[lowIdx]
                lowIdx += 1
            highSum += num
            while highIdx < i and (highSum > S or 
                                   (highSum == S and A[highIdx] == 0)):
                highSum -= A[highIdx]
                highIdx += 1
            if lowSum == S:
                res += highIdx - lowIdx + 1
        return res
            
    # TLE
    def numSubarraysWithSum0(self, A: List[int], S: int) -> int:
        left, right = 0, 0
        res, N = 0, len(A)
        for left in range(N):
            right = left
            Sum = 0
            while right < N:
                if Sum > S: break
                if Sum <= S: 
                    Sum += A[right]
                    right += 1
                if Sum == S: res += 1
        return res
            