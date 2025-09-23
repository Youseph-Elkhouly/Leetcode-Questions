class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        

        while True:
            prev = s
            s = s.replace("()", "")
            s = s.replace("[]", "")
            s = s.replace("{}", "")

            if s == prev: #no more pairs removed this round

                break

        return s == ""
