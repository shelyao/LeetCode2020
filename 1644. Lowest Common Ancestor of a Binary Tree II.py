# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or p is None or q is None: return None
        if not(self.search(root, p) and self.search(root, q)): return None
        
        def helper(root, p, q):
            if root is None or p is None or q is None: return None
            if p.val == root.val: return p
            if q.val == root.val: return q
            left = helper(root.left, p, q)
            right = helper(root.right, p, q)
            if left and right: return root
            if left: 
                return left
            if right: 
                return right
            return None

        return helper(root, p, q)   
    
    def search(self, root, p):
        if root is None: return False
        if root.val == p.val: return True
        return self.search(root.left, p) or self.search(root.right, p)
    
            