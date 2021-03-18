class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        OPEN, CLOSE = 0, 1
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append([y1, OPEN, x1, x2])
            events.append([y2, CLOSE, x1, x2])
        events.sort()
        
        def distance():
            dist = 0
            current = -1
            for x1, x2 in active:
                current = max(current, x1)
                dist += max(0, x2 - current)
                current = max(current, x2)
            return dist
        active = []
        currY = events[0][0]
        res = 0
        for y, status, x1, x2 in events:
            res += distance()*(y - currY)
            if status == OPEN:
                active.append((x1, x2))
                active.sort()
            else:
                active.remove((x1, x2))
            currY = y
        return res%(10**9 + 7)