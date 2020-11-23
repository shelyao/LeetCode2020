class Solution:
    # brute force
    def nextGreaterElement0(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for n1 in nums1:
            dq = deque(nums2)
            n2 = dq.popleft()
            while n2 != n1:
                n2 = dq.popleft()
            while dq:
                n2 = dq.popleft()
                if n2 > n1:
                    res.append(n2)
                    break
            if n2 <= n1:
                res.append(-1)
        return res
    # stack
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_map = {}
        stack = []
        res = []
        for num in nums2:
            while stack and num > stack[-1]:
                num_map[stack.pop()] = num
            stack.append(num)
        
        for num in nums1:
            if num in num_map:
                res.append(num_map[num])
            else:
                res.append(-1)
        return res