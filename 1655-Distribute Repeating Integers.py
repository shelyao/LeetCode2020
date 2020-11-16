class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        c, n = Counter(nums), len(quantity)
        left = sorted(c.values())[-n:]
        
        quantity.sort(reverse=True)
        
        def backtrack(left, quantity, customer):
            if customer == len(quantity):
                return True
            
            for i in range(len(left)):
                if left[i] >= quantity[customer]:
                    left[i] -= quantity[customer]
                    if backtrack(left, quantity, customer+1):
                        return True
                    left[i] += quantity[customer]
            return False
        
        return backtrack(left, quantity, 0)