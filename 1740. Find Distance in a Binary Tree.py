# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        if root is None or p is None or q is None: return None
        if p == q: return 0
        
        lca = self.findLCA(root, p, q)
        if not lca: return None
        
        lcaP = self.distance(lca, p)
        lcaQ = self.distance(lca, q)
        #print(lca.val, lcaP, lcaQ)
        return lcaP + lcaQ
        
    def findLCA(self, root, p, q):
        if root is None or p is None or q is None: return None
        if root.val == p or root.val == q: return root
        
        left = self.findLCA(root.left, p, q)
        right = self.findLCA(root.right, p, q)
        
        if left and right: return root
        if left: return left
        if right: return right
        return None
    
    def distance(self, lca, val):
        res = 0
        queue = deque([lca])
        while queue:
            n = len(queue)
            for i in range(n):
                curr = queue.popleft()
                if curr.val == val: return res
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            res += 1
        return res
            
        
        