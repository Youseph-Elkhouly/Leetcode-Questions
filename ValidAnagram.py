class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        

        #length of string stored in two different place holders 
        # place holder for s
        x1 = len(s)

        # place holder for t
        x2 = len(t)

        if x1 == x2:
            return sorted(s) == sorted(t)
        else:
            return False

                
            
            


