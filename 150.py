class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        #Start with an empty stack
        stack = []

        #the next step is to just check the token in the list or stack
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                #pop the top two numbers
                num2 = stack.pop()
                num1 = stack.pop()
                
                #preform the operation and push the result back into the stack

                if token == '+':
                    stack.append(num1 + num2)
                elif token == '-':
                    stack.append(num1 - num2)
                elif token == '*':
                    stack.append(num1 * num2)
                elif token == '/':
                    #we need to truncate the zero.  kind of like casting in C we are converting into an int cuts of decial part
                    result = int(float(num1) / num2)
                    stack.append(result)

            else:

                    #push numbers as integers back into the stack

                    stack.append(int(token))

        return stack[-1]
        

        
