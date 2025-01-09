class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        

        """

        if len(nums) <= 1:
            return False
   
        nums.sort()


        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True #if a duplicate is found

        return False # a duplicate is not found
            

        
