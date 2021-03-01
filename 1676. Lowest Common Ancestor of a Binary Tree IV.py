# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        if root is None: return None
        def helper(node, node1, node2):
            if node is None or node1 is None or node2 is None: return None 
            if node == node1 or node == node2: return node
            left = helper(node.left, node1, node2)
            right = helper(node.right, node1, node2)
            
            if left and right: return node
            if left: return left
            if right: return right
            
        while nodes:
            if len(nodes) == 1: return nodes[0]
            node1 = nodes.pop()
            node2 = nodes.pop()
            if node1 == root or node2 == root: return root
            node = helper(root, node1, node2)
            if node is not None:
                nodes.append(node)
        return None
        