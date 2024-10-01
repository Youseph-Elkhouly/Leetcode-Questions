#28

class Solution(object):
    def strStr(self, haystack, needle):
        
        
        #constraions 1 <= haystack.length, needle.length <= 104
        #haystack and needle consist of only lowercase English characters.

        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        return haystack.find(needle)
        
