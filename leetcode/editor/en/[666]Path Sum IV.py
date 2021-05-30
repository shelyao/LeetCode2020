# If the depth of a tree is smaller than 5, then this tree can be represented by
#  a list of three-digits integers. 
# 
#  For each integer in this list: 
# 
#  
#  The hundreds digit represents the depth D of this node, 1 <= D <= 4. 
#  The tens digit represents the position P of this node in the level it belongs
#  to, 1 <= P <= 8. The position is the same as that in a full binary tree. 
#  The units digit represents the value V of this node, 0 <= V <= 9. 
#  
# 
#  Given a list of ascending three-digits integers representing a binary tree wi
# th the depth smaller than 5, you need to return the sum of all paths from the ro
# ot towards the leaves. 
# 
#  It's guaranteed that the given list represents a valid connected binary tree.
#  
# 
#  Example 1: 
# 
#  
# Input: [113, 215, 221]
# Output: 12
# Explanation: 
# The tree that the list represents is:
#     3
#    / \
#   5   1
# 
# The path sum is (3 + 5) + (3 + 1) = 12.
#  
# 
#  
# 
#  Example 2: 
# 
#  
# Input: [113, 221]
# Output: 4
# Explanation: 
# The tree that the list represents is: 
#     3
#      \
#       1
# 
# The path sum is (3 + 1) = 4.
#  
#  Related Topics Tree 
#  👍 223 👎 304


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def pathSum(self, nums: List[int]) -> int:
        self.res = 0
        values = {x // 10: x % 10 for x in nums}

        def dfs(node, cum_sum=0):
            if node not in values: return
            cum_sum += values[node]
            depth, pos = divmod(node, 10)
            left = (depth + 1) * 10 + 2 * pos - 1
            right = left + 1
            if left not in values and right not in values:
                self.res += cum_sum
            else:
                dfs(left, cum_sum)
                dfs(right, cum_sum)

        dfs(nums[0] // 10)
        return self.res

# leetcode submit region end(Prohibit modification and deletion)
