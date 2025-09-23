class MinStack(object):

    def __init__(self):
        
        #current approach use two stack
        #One normal stack for valuea 
        #Another stack for the min values

        self.stack = [] #holds all values
        self.min_stack = []  #holds the current minimum     



    #takes in one value which is a int and pushes this value onto the stack
    def push(self, val):

        self.stack.append(val)

        # if min _stack empty or val <= current min also push to min_stack

        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

        """
        :type val: int
        :rtype: None
        """

        


    def pop(self):
        """
        :rtype: None
        """

        if self.stack:
            val = self.stack.pop()
            #if the popped value is the current min pop from min_stack too
            if val == self.min_stack[-1]:
                self.min_stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        
        return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
