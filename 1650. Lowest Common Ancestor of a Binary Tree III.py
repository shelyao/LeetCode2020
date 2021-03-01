"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        if p.parent is None: return p
        if q.parent is None: return q
        parentP = set()
        while p:
            parentP.add(p)
            p = p.parent
        
        while q:
            if q in parentP: return q
            q = q.parent
        
        return None