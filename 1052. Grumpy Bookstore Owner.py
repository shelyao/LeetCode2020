class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        if not customers or len(customers) == 0: return 0
        n = len(customers)
        n_satisfied = 0
        for i in range(n):
            if grumpy[i] == 0:
                n_satisfied += customers[i]
        if X == 0: return n_satisfied
        for i in range(X):
            if grumpy[i] == 1:
                n_satisfied += customers[i]
        
        left = 1
        res = n_satisfied
        while left < n - X + 1:
            if grumpy[left - 1] == 1:
                n_satisfied -= customers[left - 1]
            if grumpy[left + X - 1] == 1:
                n_satisfied += customers[left + X - 1]
            res = max(res, n_satisfied)
            left += 1
        return res