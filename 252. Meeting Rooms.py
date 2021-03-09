class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(len(intervals)):
            if i == 0: continue
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True
            