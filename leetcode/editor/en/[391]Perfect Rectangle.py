# Given N axis-aligned rectangles where N > 0, determine if they all together fo
# rm an exact cover of a rectangular region. 
# 
#  Each rectangle is represented as a bottom-left point and a top-right point. F
# or example, a unit square is represented as [1,1,2,2]. (coordinate of bottom-lef
# t point is (1, 1) and top-right point is (2, 2)). 
# 
#  
# 
#  Example 1: 
# 
#  
# rectangles = [
#   [1,1,3,3],
#   [3,1,4,2],
#   [3,2,4,4],
#   [1,3,2,4],
#   [2,3,3,4]
# ]
# 
# Return true. All 5 rectangles together form an exact cover of a rectangular re
# gion.
#  
# 
#  
# 
#  
# 
#  
# 
#  Example 2: 
# 
#  
# rectangles = [
#   [1,1,2,3],
#   [1,3,2,4],
#   [3,1,4,2],
#   [3,2,4,4]
# ]
# 
# Return false. Because there is a gap between the two rectangular regions.
#  
# 
#  
# 
#  
# 
#  
# 
#  Example 3: 
# 
#  
# rectangles = [
#   [1,1,3,3],
#   [3,1,4,2],
#   [1,3,2,4],
#   [3,2,4,4]
# ]
# 
# Return false. Because there is a gap in the top center.
#  
# 
#  
# 
#  
# 
#  
# 
#  Example 4: 
# 
#  
# rectangles = [
#   [1,1,3,3],
#   [3,1,4,2],
#   [1,3,2,4],
#   [2,2,4,4]
# ]
# 
# Return false. Because two of the rectangles overlap with each other.
#  
# 
#  Related Topics Line Sweep 
#  👍 453 👎 86


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        points = set()
        area = 0
        minX, minY, maxX, maxY = float('inf'), float('inf'), float('-inf'), float('-inf')
        for rectangle in rectangles:
            bl = (rectangle[0], rectangle[1])
            br = (rectangle[2], rectangle[1])
            tl = (rectangle[0], rectangle[3])
            tr = (rectangle[2], rectangle[3])
            for p in [bl, br, tl, tr]:
                if p not in points:
                    points.add(p)
                else:
                    points.remove(p)
            area += (rectangle[2]-rectangle[0])*(rectangle[3]-rectangle[1])
        if len(points) != 4: return False
        for p in points:
            minX = min(minX, p[0])
            maxX = max(maxX, p[0])
            minY = min(minY, p[1])
            maxY = max(maxY, p[1])
        return area == (maxX - minX)*(maxY - minY)
# leetcode submit region end(Prohibit modification and deletion)
