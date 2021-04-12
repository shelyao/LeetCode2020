# One way to serialize a binary tree is to use preorder traversal. When we encou
# nter a non-null node, we record the node's value. If it is a null node, we recor
# d using a sentinel value such as '#'. 
# 
#  For example, the above binary tree can be serialized to the string "9,3,4,#,#
# ,1,#,#,2,#,6,#,#", where '#' represents a null node. 
# 
#  Given a string of comma-separated values preorder, return true if it is a cor
# rect preorder traversal serialization of a binary tree. 
# 
#  It is guaranteed that each comma-separated value in the string must be either
#  an integer or a character '#' representing null pointer. 
# 
#  You may assume that the input format is always valid. 
# 
#  
#  For example, it could never contain two consecutive commas, such as "1,,3". 
#  
# 
#  
#  Example 1: 
#  Input: preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
# Output: true
#  Example 2: 
#  Input: preorder = "1,#"
# Output: false
#  Example 3: 
#  Input: preorder = "9,#,#,1"
# Output: false
#  
#  
#  Constraints: 
# 
#  
#  1 <= preorder.length <= 104 
#  preoder consist of integers in the range [0, 100] and '#' separated by commas
#  ','. 
#  
# 
#  
#  Follow up: Find an algorithm without reconstructing the tree. 
#  Related Topics Stack 
#  👍 939 👎 57


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        if preorder == "#": return True
        if preorder[0] == "#": return False
        preorderList = preorder.split(",")
        Open = 2
        for i in range(1, len(preorderList)):
            if preorderList[i] == '#':
                Open -= 1
            else:
                Open += 1
            if Open == 0: break
        return (Open == 0 and i == len(preorderList) - 1)
# leetcode submit region end(Prohibit modification and deletion)
