class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)
        answer = [1] * n    # initializing the array with 1s 
        
        # Calculate prefix product for each element   
        # in cs a prefix is a sequence of characters at the start of a string 
        #so prefix here is used to store the product of elements to the left of the current index
        prefix = 1      
        for i in range(n):  #left to right 
            answer[i] = prefix   
            prefix = prefix * nums[i]    # Update `prefix` to include the value at the current index


        # in cs a suffix is a sequence of characters at the end of a string 
        # Calculate suffix product for each element and multiply it with the prefix product
          # `suffix` will be used to store the cumulative product of elements to the right of the current index
        suffix = 1
        
        for i in range(n - 1, -1, -1):  # Loop through the array from right to left
            answer[i] = answer[i] * suffix # Multiply the existing value in `answer[i]` (prefix product) by the current `suffix` product
            suffix = suffix * nums[i]

        return answer
