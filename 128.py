class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0

         # Use a set for quick lookups
        num_set = set(nums)
        longest_streak = 0
        
        for num in num_set:

            # Check if it's the start of a sequence
            if num - 1 not in num_set:  # if there isnt any number smaller the smallest one
                current_num = num       #we have our smallest number in the array
                current_streak = 1      #hence we increment our streak 
                
                # Count the length of the sequence
                while current_num + 1 in num_set:   #while the number that is one larger than the current one is in our current array continue
                    current_num += 1    #and increment the current number and the streak
                    current_streak += 1
                
                # Update the maximum streak
                longest_streak = max(longest_streak, current_streak)    
        
        return longest_streak 
            
