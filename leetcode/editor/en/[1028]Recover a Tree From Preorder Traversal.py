# We run a preorder depth-first search (DFS) on the root of a binary tree. 
# 
#  At each node in this traversal, we output D dashes (where D is the depth of t
# his node), then we output the value of this node. If the depth of a node is D, t
# he depth of its immediate child is D + 1. The depth of the root node is 0. 
# 
#  If a node has only one child, that child is guaranteed to be the left child. 
# 
# 
#  Given the output S of this traversal, recover the tree and return its root. 
# 
#  
#  Example 1: 
# 
#  
# Input: S = "1-2--3--4-5--6--7"
# Output: [1,2,5,3,4,6,7]
#  
# 
#  Example 2: 
# 
#  
# Input: S = "1-2--3---4-5--6---7"
# Output: [1,2,5,3,null,6,null,4,null,7]
#  
# 
#  Example 3: 
# 
#  
# Input: S = "1-401--349---90--88"
# Output: [1,401,null,349,88,90]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the original tree is in the range [1, 1000]. 
#  1 <= Node.val <= 109 
#  
#  Related Topics Tree Depth-first Search 
#  👍 637 👎 22


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        if not S or len(S) == 0: return None
        start, n = 0, len(S)
        dummy_head = TreeNode()
        stack = [(dummy_head, -1)]
        current, level = "", 0
        while start < n:
            while start < n and S[start] == "-":
                level += 1
                start += 1
            while start < n and S[start].isdigit():
                current += S[start]
                start += 1
            node = TreeNode(current)
            if level > stack[-1][1]:
                stack[-1][0].left = node
            else:
                while stack[-1][1] >= level:
                    stack.pop()
                stack[-1][0].right = node
            stack.append((node, level))
            current, level = "", 0
        return dummy_head.left

# leetcode submit region end(Prohibit modification and deletion)
