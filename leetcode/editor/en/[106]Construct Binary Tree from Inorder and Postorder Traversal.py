# Given two integer arrays inorder and postorder where inorder is the inorder tr
# aversal of a binary tree and postorder is the postorder traversal of the same tr
# ee, construct and return the binary tree. 
# 
#  
#  Example 1: 
# 
#  
# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]
#  
# 
#  Example 2: 
# 
#  
# Input: inorder = [-1], postorder = [-1]
# Output: [-1]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= inorder.length <= 3000 
#  postorder.length == inorder.length 
#  -3000 <= inorder[i], postorder[i] <= 3000 
#  inorder and postorder consist of unique values. 
#  Each value of postorder also appears in inorder. 
#  inorder is guaranteed to be the inorder traversal of the tree. 
#  postorder is guaranteed to be the postorder traversal of the tree. 
#  
#  Related Topics Array Tree Depth-first Search 
#  👍 2561 👎 49


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        inOrderMap = {val: idx for idx, val in enumerate(inorder)}

        def helper(left, right):
            nonlocal postorder_idx
            if left > right: return None

            root_val = postorder[postorder_idx]
            root = TreeNode(root_val)
            postorder_idx -= 1

            root.right = helper(inOrderMap[root_val] + 1, right)
            root.left = helper(left, inOrderMap[root_val] - 1)

            return root

        postorder_idx = len(postorder) - 1
        return helper(0, len(postorder) - 1)
# leetcode submit region end(Prohibit modification and deletion)
