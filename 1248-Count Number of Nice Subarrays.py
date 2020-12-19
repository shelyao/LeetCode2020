class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        oddsList = [-1]
        res = 0
        for i, num in enumerate(nums):
            if num%2 != 0: oddsList.append(i)
        oddsList.append(len(nums))
        N = len(oddsList)
        if N-2 < k: return 0
        for i in range(1, N-k):
            res += (oddsList[i] - oddsList[i-1])*(oddsList[i+k]-oddsList[i+k-1])
        return res