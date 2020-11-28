class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        mod = (10**9 + 7)
        stack = []
        left, right = [0]*n, [0]*n
        for i in range(n):
            count = 1
            while stack and arr[i] < stack[-1][0]:
                count += stack.pop()[1]
            left[i] = count    
            stack.append((arr[i], count))
        stack = []
        for i in range(n-1, -1, -1):
            count = 1
            while stack and arr[i] <= stack[-1][0]:
                count += stack.pop()[1]
            right[i] = count
            stack.append((arr[i], count)) 
        return sum(num*l*r for num, l, r in zip(arr, left, right))%mod
    
    
    
    #brute force
    def sumSubarrayMins0(self, arr: List[int]) -> int:
        dq = deque(arr.copy())
        res = sum(dq)
        while dq: 
            length = len(dq)
            for i in range(length - 1):
                current = dq.popleft()
                if not dq:
                    res += current
                else:
                    if current > dq[0]:
                        res += dq[0]
                        dq.append(dq[0])
                    else:
                        dq.append(current)
                        res += current
            dq.popleft()
        
        return res%(10**9 + 7)
        