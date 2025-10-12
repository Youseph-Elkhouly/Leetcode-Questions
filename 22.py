class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        

        result = []

        def helper(current, open_count, closed_count):
            #if the string is done we have used all the parenthesis
            if len(current) == 2 * n:

                result.append(current)

                return

            #we add. "(" if we still have remaining brackets left
            if open_count < n:
                helper(current + "(", open_count + 1, closed_count)

            #we can add ")" if there are more "(" than ")"
            if closed_count < open_count:
                helper(current + ")", open_count, closed_count + 1)

        helper("", 0 , 0)
        return result


        
