# Given the root of a complete binary tree, return the number of the nodes in th
# e tree. 
# 
#  According to Wikipedia, every level, except possibly the last, is completely 
# filled in a complete binary tree, and all nodes in the last level are as far lef
# t as possible. It can have between 1 and 2h nodes inclusive at the last level h.
#  
# 
#  
#  Example 1: 
# 
#  
# Input: root = [1,2,3,4,5,6]
# Output: 6
#  
# 
#  Example 2: 
# 
#  
# Input: root = []
# Output: 0
#  
# 
#  Example 3: 
# 
#  
# Input: root = [1]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 5 * 104]. 
#  0 <= Node.val <= 5 * 104 
#  The tree is guaranteed to be complete. 
#  
# 
#  
# Follow up: Traversing the tree to count the number of nodes in the tree is an 
# easy solution but with O(n) complexity. Could you find a faster algorithm? Relat
# ed Topics Binary Search Tree 
#  👍 2878 👎 258


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        left = self.getDepth(root, 1)
        right = self.getDepth(root, 0)
        if left == right:
            return 2**left - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    def getDepth(self, root, left = 1):
        if not root: return 0
        if left:
            return 1 + self.getDepth(root.left, 1)
        else:
            return 1 + self.getDepth(root.right, 0)

# leetcode submit region end(Prohibit modification and deletion)
