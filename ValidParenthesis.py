class Solution(object):
    def isValid(self, s):
        

        stack = []

        bracket_map = { "}": "{", ")": "(", "]": "["}

        for char in s:
            if char in ("(", "{", "["):
                stack.append(char)
            if char in (")", "}", "]"):
                if stack and (stack[-1] == bracket_map[char]):
                    stack.pop()
                else: 
                    return False
            if not stack: 
                return True

        
        
        """
        :type s: str
        :rtype: bool
        """
        
