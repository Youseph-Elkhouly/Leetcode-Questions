class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        

        """



        counter = 0
        nums.sort()

        for counter in range(len(nums) - 1):

            if nums[counter] == nums[counter + 1]:
                return True #if a duplicate is found

            return False # a duplicate is not found
            

        
