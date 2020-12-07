class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack, res = [], [0]*n
        for log in logs:
            function_id, action, timestamp = log.split(':')
            if action == "start":
                if stack:
                    res[int(stack[-1][0])] += int(timestamp) - stack[-1][1]
                stack.append([function_id, int(timestamp)])
            else:
                res[int(stack[-1][0])] += int(timestamp) - stack[-1][1] + 1
                stack.pop()
                if stack:
                    stack[-1][1] = int(timestamp) + 1
        
        return res