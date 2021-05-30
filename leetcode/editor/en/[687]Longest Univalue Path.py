# Given the root of a binary tree, return the length of the longest path, where 
# each node in the path has the same value. This path may or may not pass through 
# the root. 
# 
#  The length of the path between two nodes is represented by the number of edge
# s between them. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [5,4,5,1,1,5]
# Output: 2
#  
# 
#  Example 2: 
# 
#  
# Input: root = [1,4,5,4,4,5]
# Output: 2
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 104]. 
#  -1000 <= Node.val <= 1000 
#  The depth of the tree will not exceed 1000. 
#  
#  Related Topics Tree Recursion 
#  👍 2295 👎 559


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.res = 0
        def helper(root):
            if not root: return 0
            left_len = helper(root.left)
            right_len = helper(root.right)
            left = right = 0
            if root.left and root.val == root.left.val:
                left = left_len + 1
            if root.right and root.val == root.right.val:
                right = right_len + 1
            self.res = max(self.res, left + right)
            return max(left, right)
        helper(root)
        return self.res
# leetcode submit region end(Prohibit modification and deletion)
