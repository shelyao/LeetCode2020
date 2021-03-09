class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        n1, n2 = len(firstList), len(secondList)
        p1 = p2 = 0
        res = []
        while p1 < n1 and p2 < n2:
            if firstList[p1][0] <= secondList[p2][1] or secondList[p2][0] <= firstList[p1][1]:
                left = max(firstList[p1][0], secondList[p2][0])
                right = min(firstList[p1][1], secondList[p2][1])
                if right >= left:
                    res.append([left, right])
            if firstList[p1][1] >= secondList[p2][1]:
                p2 += 1
            else:
                p1 += 1
        return res