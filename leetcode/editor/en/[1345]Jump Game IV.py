# Given an array of integers arr, you are initially positioned at the first inde
# x of the array. 
# 
#  In one step you can jump from index i to index: 
# 
#  
#  i + 1 where: i + 1 < arr.length. 
#  i - 1 where: i - 1 >= 0. 
#  j where: arr[i] == arr[j] and i != j. 
#  
# 
#  Return the minimum number of steps to reach the last index of the array. 
# 
#  Notice that you can not jump outside of the array at any time. 
# 
#  
#  Example 1: 
# 
#  
# Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
# Output: 3
# Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that in
# dex 9 is the last index of the array.
#  
# 
#  Example 2: 
# 
#  
# Input: arr = [7]
# Output: 0
# Explanation: Start index is the last index. You don't need to jump.
#  
# 
#  Example 3: 
# 
#  
# Input: arr = [7,6,9,6,9,6,9,7]
# Output: 1
# Explanation: You can jump directly from index 0 to index 7 which is last index
#  of the array.
#  
# 
#  Example 4: 
# 
#  
# Input: arr = [6,1,9]
# Output: 2
#  
# 
#  Example 5: 
# 
#  
# Input: arr = [11,22,7,7,7,7,7,7,7,22,13]
# Output: 3
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= arr.length <= 5 * 104 
#  -108 <= arr[i] <= 108 
#  
#  Related Topics Breadth-first Search 
#  👍 653 👎 44


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1: return 0
        if arr[0] == arr[-1]: return 1
        arrMap = defaultdict(list)
        seen = set()
        seen.add(0)
        for i, x in enumerate(arr):
            arrMap[x].append(i)
        stack = deque([0])
        res = 0
        while stack:
            #print(stack, n)
            k = len(stack)
            for i in range(k):
                curr = stack.popleft()
                if curr == n-1: return res
                if curr + 1 < n and curr + 1 not in seen:
                    seen.add(curr+1)
                    stack.append(curr+1)
                if curr - 1 >= 0 and curr - 1 not in seen:
                    seen.add(curr-1)
                    stack.append(curr-1)
                for a in arrMap[arr[curr]]:
                    if a not in seen:
                        seen.add(a)
                        stack.append(a)
                arrMap[arr[curr]].clear()
            res += 1
        return -1
# leetcode submit region end(Prohibit modification and deletion)
