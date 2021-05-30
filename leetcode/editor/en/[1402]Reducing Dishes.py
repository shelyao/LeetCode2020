# A chef has collected data on the satisfaction level of his n dishes. Chef can 
# cook any dish in 1 unit of time. 
# 
#  Like-time coefficient of a dish is defined as the time taken to cook that dis
# h including previous dishes multiplied by its satisfaction level i.e. time[i]*sa
# tisfaction[i] 
# 
#  Return the maximum sum of Like-time coefficient that the chef can obtain afte
# r dishes preparation. 
# 
#  Dishes can be prepared in any order and the chef can discard some dishes to g
# et this maximum value. 
# 
#  
#  Example 1: 
# 
#  
# Input: satisfaction = [-1,-8,0,5,-9]
# Output: 14
# Explanation: After Removing the second and last dish, the maximum total Like-t
# ime coefficient will be equal to (-1*1 + 0*2 + 5*3 = 14). Each dish is prepared 
# in one unit of time. 
# 
#  Example 2: 
# 
#  
# Input: satisfaction = [4,3,2]
# Output: 20
# Explanation: Dishes can be prepared in any order, (2*1 + 3*2 + 4*3 = 20)
#  
# 
#  Example 3: 
# 
#  
# Input: satisfaction = [-1,-4,-5]
# Output: 0
# Explanation: People don't like the dishes. No dish is prepared.
#  
# 
#  Example 4: 
# 
#  
# Input: satisfaction = [-2,5,-1,0,3,-3]
# Output: 35
#  
# 
#  
#  Constraints: 
# 
#  
#  n == satisfaction.length 
#  1 <= n <= 500 
#  -10^3 <= satisfaction[i] <= 10^3 
#  Related Topics Dynamic Programming 
#  👍 480 👎 93


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        if satisfaction[-1] <= 0: return 0
        res = 0
        total = 0
        for i, s in enumerate(satisfaction):
            res += s*(i+1)
            total += s
        for i, s in enumerate(satisfaction):
            _next = res - total
            total -= s
            if _next <= res: break
            res = _next
        return res
# leetcode submit region end(Prohibit modification and deletion)
