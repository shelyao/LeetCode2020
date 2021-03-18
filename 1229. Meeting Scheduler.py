class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        p1 = p2 = 0
        n1, n2 = len(slots1), len(slots2)
        while p1 < n1 and p2 < n2:
            s1, s2 = slots1[p1], slots2[p2]
            if s1[0] <= s2[0] < s1[1]:
                if min(s1[1], s2[1]) - s2[0] >= duration:
                    return [s2[0], s2[0] + duration]
            if s2[0] <= s1[0] < s2[1]:
                if min(s1[1], s2[1]) - s1[0] >= duration:
                    return [s1[0], s1[0] + duration]
            if s1[1] >= s2[1]:
                p2 += 1
            else:
                p1 += 1
        return []
        