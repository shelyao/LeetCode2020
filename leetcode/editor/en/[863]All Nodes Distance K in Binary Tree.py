# We are given a binary tree (with root node root), a target node, and an intege
# r value K. 
# 
#  Return a list of the values of all nodes that have a distance K from the targ
# et node. The answer can be returned in any order. 
# 
#  
# 
#  
#  
# 
#  
#  Example 1: 
# 
#  
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
# 
# Output: [7,4,1]
# 
# Explanation: 
# The nodes that are a distance 2 from the target node (with value 5)
# have values 7, 4, and 1.
# 
# 
# 
# Note that the inputs "root" and "target" are actually TreeNodes.
# The descriptions of the inputs above are just serializations of these objects.
# 
#  
# 
#  
# 
#  Note: 
# 
#  
#  The given tree is non-empty. 
#  Each node in the tree has unique values 0 <= node.val <= 500. 
#  The target node is a node in the tree. 
#  0 <= K <= 1000. 
#  
#  
#  Related Topics Tree Depth-first Search Breadth-first Search 
#  👍 3550 👎 73


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque, defaultdict
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        treeMap = defaultdict(list)
        queue = deque([root])
        if K == 0: return [target.val]
        while queue:
            node = queue.popleft()
            if node.left:
                treeMap[node.val].append(node.left.val)
                treeMap[node.left.val].append(node.val)
                queue.append(node.left)
            if node.right:
                treeMap[node.val].append(node.right.val)
                treeMap[node.right.val].append(node.val)
                queue.append(node.right)
        queue = deque(treeMap[target.val])
        visited = set()
        while K > 1:
            n = len(queue)
            for i in range(n):
                val = queue.popleft()
                if val in visited: continue
                visited.add(val)
                for nb in treeMap[val]:
                    if nb not in visited and nb != target.val:
                        queue.append(nb)
            K -= 1
        return list(set(queue))
# leetcode submit region end(Prohibit modification and deletion)
