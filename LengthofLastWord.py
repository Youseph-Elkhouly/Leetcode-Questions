class Solution(object):
    def lengthOfLastWord(self, s):
        # Step 1: Remove any extra spaces from the end of the string
        s = s.rstrip()                  # This removes spaces from the right end of the string

        # Step 2: Split the string into a list of words based on spaces
        words = s.split()               # This splits the string by spaces

        # Step 3: Get the last word in the list and return its length
        last_word = words[-1]           # The last word is at the last position
        return len(last_word)           # Return the length of the last word


        """
        :type s: str
        :rtype: int
        """
