# Implement the RandomizedCollection class: 
# 
#  
#  RandomizedCollection() Initializes the RandomizedCollection object. 
#  bool insert(int val) Inserts an item val into the multiset if not present. Re
# turns true if the item was not present, false otherwise. 
#  bool remove(int val) Removes an item val from the multiset if present. Return
# s true if the item was present, false otherwise. Note that if val has multiple o
# ccurrences in the multiset, we only remove one of them. 
#  int getRandom() Returns a random element from the current multiset of element
# s (it's guaranteed that at least one element exists when this method is called).
#  The probability of each element being returned is linearly related to the numbe
# r of same values the multiset contains. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input
# ["RandomizedCollection", "insert", "insert", "insert", "getRandom", "remove", 
# "getRandom"]
# [[], [1], [1], [2], [], [1], []]
# Output
# [null, true, false, true, 2, true, 1]
# 
# Explanation
# RandomizedCollection randomizedCollection = new RandomizedCollection();
# randomizedCollection.insert(1);   // return True. Inserts 1 to the collection.
#  Returns true as the collection did not contain 1.
# randomizedCollection.insert(1);   // return False. Inserts another 1 to the co
# llection. Returns false as the collection contained 1. Collection now contains [
# 1,1].
# randomizedCollection.insert(2);   // return True. Inserts 2 to the collection,
#  returns true. Collection now contains [1,1,2].
# randomizedCollection.getRandom(); // getRandom should return 1 with the probab
# ility 2/3, and returns 2 with the probability 1/3.
# randomizedCollection.remove(1);   // return True. Removes 1 from the collectio
# n, returns true. Collection now contains [1,2].
# randomizedCollection.getRandom(); // getRandom should return 1 and 2 both equa
# lly likely.
#  
# 
#  
#  Constraints: 
# 
#  
#  -231 <= val <= 231 - 1 
#  At most 105 calls will be made to insert, remove, and getRandom. 
#  There will be at least one element in the data structure when getRandom is ca
# lled. 
#  
# 
#  
# Follow up: Could you implement the functions of the class with each function w
# orks in average O(1) time? Related Topics Array Hash Table Design 
#  👍 1121 👎 90


# leetcode submit region begin(Prohibit modification and deletion)
class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._dict = {}
        self._list = []
        self._n = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self._list.append(val)
        self._n += 1
        if val not in self._dict:
            self._dict[val] = [self._n - 1]
            return True
        else:
            self._dict[val].append(self._n - 1)
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self._dict: return False
        else:
            self._n -= 1
            idx, last_num = self._dict[val][-1], self._list[-1]
            self._list[idx], self._dict[last_num][-1] = last_num, idx
            self._dict[val].pop()
            self._list.pop()
            if self._dict[val] == []: del self._dict[val]
            if last_num in self._dict: self._dict[last_num].sort()
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self._list)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# leetcode submit region end(Prohibit modification and deletion)
