# Given an array nums and two types of queries where you should update the value
#  of an index in the array, and retrieve the sum of a range in the array. 
# 
#  Implement the NumArray class: 
# 
#  
#  NumArray(int[] nums) initializes the object with the integer array nums. 
#  void update(int index, int val) updates the value of nums[index] to be val. 
#  int sumRange(int left, int right) returns the sum of the subarray nums[left, 
# right] (i.e., nums[left] + nums[left + 1], ..., nums[right]). 
#  
# 
#  
#  Example 1: 
# 
#  
# Input
# ["NumArray", "sumRange", "update", "sumRange"]
# [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
# Output
# [null, 9, null, 8]
# 
# Explanation
# NumArray numArray = new NumArray([1, 3, 5]);
# numArray.sumRange(0, 2); // return 9 = sum([1,3,5])
# numArray.update(1, 2);   // nums = [1,2,5]
# numArray.sumRange(0, 2); // return 8 = sum([1,2,5])
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 3 * 104 
#  -100 <= nums[i] <= 100 
#  0 <= index < nums.length 
#  -100 <= val <= 100 
#  0 <= left <= right < nums.length 
#  At most 3 * 104 calls will be made to update and sumRange. 
#  
#  Related Topics Binary Indexed Tree Segment Tree 
#  👍 1781 👎 106


# leetcode submit region begin(Prohibit modification and deletion)
class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        if self.n > 0:
            self.tree = self.buildTree(nums)

    def update(self, index: int, val: int) -> None:
        pos = index + self.n
        self.tree[pos] = val
        while pos > 0:
            if pos%2 == 0:
                pos = pos//2
            else:
                pos = (pos-1)//2
            self.tree[pos] = self.tree[pos*2] + self.tree[pos*2+1]

    def sumRange(self, left: int, right: int) -> int:
        left += self.n
        right += self.n
        res = 0
        while left <= right:
            if left % 2 == 1:
                res += self.tree[left]
                left += 1
            if right % 2 == 0:
                res += self.tree[right]
                right -= 1
            left = left//2
            right = right//2
        return res

    def buildTree(self, nums):
        n = len(nums)
        tree = [0]*2*n
        for i in range(n, 2*n):
            tree[i] = nums[i-n]
        for i in range(n-1, 0, -1):
            tree[i] = tree[i*2] + tree[i*2+1]
        return tree


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
# leetcode submit region end(Prohibit modification and deletion)
