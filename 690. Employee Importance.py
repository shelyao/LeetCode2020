"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        id_index = {x.id:i for i, x in enumerate(employees)}
        dq = deque([employees[id_index[id]]])
        res = 0
        while dq:
            current = dq.popleft()
            res += current.importance
            for sub in current.subordinates:
                new_i = id_index[sub]
                dq.append(employees[new_i])
        return res