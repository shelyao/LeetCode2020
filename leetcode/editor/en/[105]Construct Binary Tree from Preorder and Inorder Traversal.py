# Given two integer arrays preorder and inorder where preorder is the preorder t
# raversal of a binary tree and inorder is the inorder traversal of the same tree,
#  construct and return the binary tree. 
# 
#  
#  Example 1: 
# 
#  
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
#  
# 
#  Example 2: 
# 
#  
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= preorder.length <= 3000 
#  inorder.length == preorder.length 
#  -3000 <= preorder[i], inorder[i] <= 3000 
#  preorder and inorder consist of unique values. 
#  Each value of inorder also appears in preorder. 
#  preorder is guaranteed to be the preorder traversal of the tree. 
#  inorder is guaranteed to be the inorder traversal of the tree. 
#  
#  Related Topics Array Tree Depth-first Search 
#  👍 4992 👎 128


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inOrderMap = {val: idx for idx, val in enumerate(inorder)}

        def helper(left, right):
            nonlocal preorder_index
            if left > right: return None

            root_val = preorder[preorder_index]
            root = TreeNode(root_val)
            preorder_index += 1

            root.left = helper(left, inOrderMap[root_val] - 1)
            root.right = helper(inOrderMap[root_val] + 1, right)
            return root

        preorder_index = 0
        return helper(0, len(preorder) - 1)
# leetcode submit region end(Prohibit modification and deletion)
