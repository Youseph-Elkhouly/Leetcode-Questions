class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
       
        #init another array of zeros
        result = [0] * len(temperatures)

        #init a empty stack
        stack = []

        # loop through each temperature by its index
        for i in range(len(temperatures)):


            # while the stack is not empty AND the current day is warmer
            while stack and temperatures[i] > temperatures[stack[-1]]:
            
                prev_day = stack.pop()              # take the last day off the stack
            
                result[prev_day] = i - prev_day     # how many days until it got warmer

            # push the current day's index onto the stack
            stack.append(i)
        
        return result
