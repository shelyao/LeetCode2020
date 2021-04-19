# Implement a SnapshotArray that supports the following interface: 
# 
#  
#  SnapshotArray(int length) initializes an array-like data structure with the g
# iven length. Initially, each element equals 0. 
#  void set(index, val) sets the element at the given index to be equal to val. 
# 
#  int snap() takes a snapshot of the array and returns the snap_id: the total n
# umber of times we called snap() minus 1. 
#  int get(index, snap_id) returns the value at the given index, at the time we 
# took the snapshot with the given snap_id 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: ["SnapshotArray","set","snap","set","get"]
# [[3],[0,5],[],[0,6],[0,0]]
# Output: [null,null,0,null,5]
# Explanation: 
# SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
# snapshotArr.set(0,5);  // Set array[0] = 5
# snapshotArr.snap();  // Take a snapshot, return snap_id = 0
# snapshotArr.set(0,6);
# snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= length <= 50000 
#  At most 50000 calls will be made to set, snap, and get. 
#  0 <= index < length 
#  0 <= snap_id < (the total number of times we call snap()) 
#  0 <= val <= 10^9 
#  
#  Related Topics Array 
#  👍 834 👎 160


# leetcode submit region begin(Prohibit modification and deletion)
class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self._array = [{0:0} for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        self._array[index][self.snap_id] = val

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        if snap_id in self._array[index]:
            return self._array[index][snap_id]
        ids = list(self._array[index].keys())
        left, right = 0, len(ids) - 1
        while left < right - 1:
            mid = left + (right - left)//2
            if ids[mid] > snap_id:
                right = mid - 1
            else:
                left = mid
        if ids[right] < snap_id: return self._array[index][ids[right]]
        return self._array[index][ids[left]]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
# leetcode submit region end(Prohibit modification and deletion)
