# Design and implement a data structure for a Least Frequently Used (LFU) cache.
#  
# 
#  Implement the LFUCache class: 
# 
#  
#  LFUCache(int capacity) Initializes the object with the capacity of the data s
# tructure. 
#  int get(int key) Gets the value of the key if the key exists in the cache. Ot
# herwise, returns -1. 
#  void put(int key, int value) Update the value of the key if present, or inser
# ts the key if not already present. When the cache reaches its capacity, it shoul
# d invalidate and remove the least frequently used key before inserting a new ite
# m. For this problem, when there is a tie (i.e., two or more keys with the same f
# requency), the least recently used key would be invalidated. 
#  
# 
#  To determine the least frequently used key, a use counter is maintained for e
# ach key in the cache. The key with the smallest use counter is the least frequen
# tly used key. 
# 
#  When a key is first inserted into the cache, its use counter is set to 1 (due
#  to the put operation). The use counter for a key in the cache is incremented ei
# ther a get or put operation is called on it. 
# 
#  
#  Example 1: 
# 
#  
# Input
# ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "g
# et"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, 3, null, -1, 3, 4]
# 
# Explanation
# // cnt(x) = the use counter for key x
# // cache=[] will show the last used order for tiebreakers (leftmost element is
#   most recent)
# LFUCache lfu = new LFUCache(2);
# lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
# lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
# lfu.get(1);      // return 1
#                  // cache=[1,2], cnt(2)=1, cnt(1)=2
# lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalid
# ate 2.
#                  // cache=[3,1], cnt(3)=1, cnt(1)=2
# lfu.get(2);      // return -1 (not found)
# lfu.get(3);      // return 3
#                  // cache=[3,1], cnt(3)=2, cnt(1)=2
# lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1
# .
#                  // cache=[4,3], cnt(4)=1, cnt(3)=2
# lfu.get(1);      // return -1 (not found)
# lfu.get(3);      // return 3
#                  // cache=[3,4], cnt(4)=1, cnt(3)=3
# lfu.get(4);      // return 4
#                  // cache=[3,4], cnt(4)=2, cnt(3)=3
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= capacity, key, value <= 104 
#  At most 105 calls will be made to get and put. 
#  
# 
#  
# Follow up: Could you do both operations in O(1) time complexity? Related Topic
# s Design 
#  👍 1957 👎 150


# leetcode submit region begin(Prohibit modification and deletion)
class LFUCache:
## Main Data cache: Normal Dict with {key: [value, frequency]}
## Frequency cache: Default Dict {frequency: [key1, key2, key3]} all the keys with same frequency and frequency as key.
    def __init__(self, capacity: int):
        self.freqDict = defaultdict(list)
        self._cache = {}
        self.maxCap = capacity

    def get(self, key: int) -> int:
        res = self._cache.get(key, -1)
        if res == -1: return -1
        else:
            val, freq = res[0], res[1]
            self.freqDict[freq].remove(key)
            if not self.freqDict[freq]:
                del self.freqDict[freq]
            self.freqDict[freq + 1].append(key)
            self._cache[key] = [val, freq + 1]
        return val

    def put(self, key: int, value: int) -> None:
        if self.maxCap <= 0: return
        if key in self._cache:
            res = self._cache[key]
            val, freq = res[0], res[1]
            self.freqDict[freq].remove(key)
            if not self.freqDict[freq]:
                del self.freqDict[freq]
            self.freqDict[freq + 1].append(key)
            self._cache[key] = [value, freq + 1]
        else:
            if len(self._cache) == self.maxCap:
                minFreq, minList = min(self.freqDict.items(), key = lambda x:x[0])
                todelete = minList[0]
                del self._cache[todelete]
                self.freqDict[minFreq].remove(todelete)
            self._cache[key] = [value, 1]
            self.freqDict[1].append(key)

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)
