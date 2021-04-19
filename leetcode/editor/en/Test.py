
# leetcode submit region begin(Prohibit modification and deletion)
class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counts = []
        self._keys = {}
        self._n = 0

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key not in self._keys:
            self.counts.append([1, key])
            self._keys[key] = self._n
            self._n += 1
        else:
            idx = self._keys[key]
            self.counts[idx][0] += 1
            cnt = self.counts[idx][0]
            replace_idx = idx - 1
            while replace_idx >= 0 and self.counts[replace_idx][0] < cnt:
                replace_key = self.counts[replace_idx][1]
                self.counts[replace_idx], self.counts[idx] = self.counts[idx], self.counts[replace_idx]
                self._keys[replace_key] += 1
                self._keys[key] -= 1
                replace_idx -= 1
                idx -= 1

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        idx = self._keys[key]
        if self.counts[idx][0] == 1:
            self.counts.pop(idx)
            self._n -= 1
            del self._keys[key]
            for i in range(idx, self._n):
                temp = self.counts[i][1]
                self._keys[temp] -= 1
        else:
            self.counts[idx][0] -= 1
            cnt = self.counts[idx][0]
            replace_idx = idx + 1
            while replace_idx < self._n and self.counts[replace_idx][0] > cnt:
                replace_key = self.counts[replace_idx][1]
                self.counts[idx], self.counts[replace_idx]  = self.counts[replace_idx], self.counts[idx]
                self._keys[replace_key] -= 1
                self._keys[key] += 1
                replace_idx += 1
                idx += 1

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if self._n > 0:
            return self.counts[0][1]
        return ""

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if self._n > 0:
            return self.counts[-1][1]
        return ""


# Your AllOne object will be instantiated and called as such:
obj = AllOne()
obj.inc("hello")
obj.inc("world")
obj.inc("leet")
obj.inc("code")
obj.inc("ds")
print(obj.counts, obj._keys)
obj.inc("leet")
print(obj.counts, obj._keys)
param_3 = obj.getMaxKey()
param_4 = obj.getMinKey()