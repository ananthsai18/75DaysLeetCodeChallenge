class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = [] # This will store indices: [index1, index2, ...]
        
        for i in range(n):
            current_temp = temperatures[i]
            
            # While the stack is not empty AND 
            # the current temperature is warmer than the temperature at the top of the stack
            while stack and current_temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                # The number of days to wait is the difference between indices
                ans[prev_index] = i - prev_index
                
            # Always push the current index onto the stack
            stack.append(i)
            
        return ans