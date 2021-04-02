# You are given an integer array stations that represents the positions of the g
# as stations on the x-axis. You are also given an integer k. 
# 
#  You should add k new gas stations. You can add the stations anywhere on the x
# -axis, and not necessarily on an integer position. 
# 
#  Let penalty() be the maximum distance between adjacent gas stations after add
# ing the k new stations. 
# 
#  Return the smallest possible value of penalty(). Answers within 10-6 of the a
# ctual answer will be accepted. 
# 
#  
#  Example 1: 
#  Input: stations = [1,2,3,4,5,6,7,8,9,10], k = 9
# Output: 0.50000
#  Example 2: 
#  Input: stations = [23,24,36,39,46,56,57,65,84,98], k = 1
# Output: 14.00000
#  
#  
#  Constraints: 
# 
#  
#  10 <= stations.length <= 2000 
#  0 <= stations[i] <= 108 
#  stations is sorted in a strictly increasing order. 
#  1 <= k <= 106 
#  
#  Related Topics Binary Search 
#  👍 425 👎 64


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        intervals = []
        for i in range(1, len(stations)):
            intervals.append(stations[i] - stations[i-1])
        l, r = 0, max(intervals)
        res = r
        while l < r - 0.1**6:
            mid = l + (r - l) / 2
            cnt = 0
            min_int = 0
            for Int in intervals:
                if Int > mid:
                    cnt += math.ceil(Int / mid) - 1
                    min_int = max(min_int, Int/math.ceil(Int/mid))
                else:
                    min_int = max(min_int, Int)
                if cnt > k: break
            # print(cnt, mid)
            if cnt <= k:
                res = min(res, min_int)
                r = mid
            else:
                l = mid
        return res
# leetcode submit region end(Prohibit modification and deletion)
