class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        #we want to take the target and subract the current index and then search for the result      

        
        def binary_search(left, right, target):
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] == target:
                    return mid
                elif numbers[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1   

        for i in range(len(numbers)):
            complement = target - numbers[i]
            found_index = binary_search(i + 1, len(numbers) - 1, complement)
            if found_index != -1:
                return [i + 1, found_index + 1] 

        
