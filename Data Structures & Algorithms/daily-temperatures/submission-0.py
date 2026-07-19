class Solution:
    def helper(self, stack, val):
        
        if stack[-1] < val:
            stack.pop()
            return 1
        else:
            helper
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        # monotonically decreasing stack
        stack = [] # to store idx of respective temperatures
        result = [0 for i in range(n)]

        stack.append(0)
        for i in range(1, n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                idx = stack.pop()
                # diff b/w indices
                result[idx] = i - idx
            stack.append(i)
        
        return result

            
       

        