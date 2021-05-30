# Given a string s of lowercase letters, you need to find the maximum number of 
# non-empty substrings of s that meet the following conditions: 
# 
#  
#  The substrings do not overlap, that is for any two substrings s[i..j] and s[k
# ..l], either j < k or i > l is true. 
#  A substring that contains a certain character c must also contain all occurre
# nces of c. 
#  
# 
#  Find the maximum number of substrings that meet the above conditions. If ther
# e are multiple solutions with the same number of substrings, return the one with
#  minimum total length. It can be shown that there exists a unique solution of mi
# nimum total length. 
# 
#  Notice that you can return the substrings in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "adefaddaccc"
# Output: ["e","f","ccc"]
# Explanation: The following are all the possible substrings that meet the condi
# tions:
# [
#   "adefaddaccc"
#   "adefadda",
#   "ef",
#   "e",
#   "f",
#   "ccc",
# ]
# If we choose the first string, we cannot choose anything else and we'd get onl
# y 1. If we choose "adefadda", we are left with "ccc" which is the only one that 
# doesn't overlap, thus obtaining 2 substrings. Notice also, that it's not optimal
#  to choose "ef" since it can be split into two. Therefore, the optimal way is to
#  choose ["e","f","ccc"] which gives us 3 substrings. No other solution of the sa
# me number of substrings exist.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "abbaccd"
# Output: ["d","bb","cc"]
# Explanation: Notice that while the set of substrings ["d","abba","cc"] also ha
# s length 3, it's considered incorrect since it has larger total length.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10^5 
#  s contains only lowercase English letters. 
#  
#  Related Topics Greedy 
#  👍 352 👎 47


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        letters = set(s)
        n = len(s)
        indices = {}
        substrs = []
        res = []
        ## get left/right index for all characters
        for i, x in enumerate(s):
            if x not in indices:
                indices[x] = [i]
        for i in range(n - 1, -1, -1):
            if len(indices[s[i]]) == 1:
                indices[s[i]].append(i)
        for a in letters:
            extended = {a: 1}
            la, ra = indices[a][0], indices[a][1]
            stack = list(set(s[la:ra + 1]) - set([a]))
            while stack:
                b = stack.pop()
                if b in extended: continue
                extended[b] = 1
                lb, rb = indices[b][0], indices[b][1]
                if la < lb < ra or la < rb < ra or (b in s[la:ra + 1]):
                    la = min(la, lb)
                    ra = max(ra, rb)
                stack.extend(list(set(s[la:ra + 1]) - set([a]) - set(extended.keys())))
            heappush(substrs, (ra - la, (la, ra)))
        while substrs:
            _, idx = heappop(substrs)
            to_add = True
            curr = s[idx[0]:idx[1] + 1]
            for e in res:
                if e in curr:
                    to_add = False
                    break
            if to_add: res.append(curr)
        # print(res)
        return res

# leetcode submit region end(Prohibit modification and deletion)
