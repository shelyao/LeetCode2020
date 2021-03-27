class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        if not arr or len(arr) <= 1: return 0
        n = len(arr)
        subleft = 0
        subright = n - 1
        while subleft < n - 1:
            if arr[subleft + 1] < arr[subleft]:
                break
            subleft += 1
        if subleft == n - 1: return 0
        while subright > 0:
            if arr[subright - 1] > arr[subright]:
                break
            subright -= 1
        if subright == n - 1: return n - subleft - 1 - (arr[subright] >= arr[subleft])
        
        def bisect(val, left, right):
            while left < right:
                mid = left + (right - left)//2
                if arr[mid] < val:
                    left = mid + 1
                else:
                    right = mid
            return right
                
        res = min(subright, n - subleft - 1)
        for i in range(subleft + 1):
            left_val = arr[i]
            right_start = bisect(left_val, subright, n-1)
            res = min(res, right_start - i - 1 + (arr[right_start] < arr[i]))
        return res
            