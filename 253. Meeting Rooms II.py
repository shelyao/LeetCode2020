class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        minHeap = []
        for i, interval in enumerate(intervals):
            if i == 0:
                res += 1
                heappush(minHeap, interval[1])
            else:
                if minHeap[0] <= interval[0]:
                    heappop(minHeap)
                else:
                    res += 1
                heappush(minHeap, interval[1])            
        return res