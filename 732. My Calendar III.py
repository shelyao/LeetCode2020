class MyCalendarThree:

    def __init__(self):
        self.overlap = Counter()

    def book(self, start: int, end: int) -> int:
        self.overlap[start] += 1
        self.overlap[end] -= 1
        res = active = 0
        for x in sorted(self.overlap):
            active += self.overlap[x]
            if active > res: res = active
        return res


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)