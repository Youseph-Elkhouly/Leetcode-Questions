class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        #Initizalize the pointers
        left = 0  #points to the first element
        right = len(height) - 1     # points to the last element 


        #Calculating the area and keeping track of it
        area = 0

        #while loop to check the pointers until they meet
        while left < right:
            #first its going to check [0, 8]

            #caclulate the area

            #width
            width = right - left 

            #height
            min_height = min(height[left], height[right])
            
            #area formula
            current_area = width * min_height

            #update area

            area = max(area, current_area)

            # Move the pointer with the smaller height

            #if your height of left pointer is less than height of right pointer, move left pointer to the right
            if height[left] < height[right]:
                left += 1
            #if your height of right pointer is greater than height of left pointer, move right pointer to the left
            else:
                right -= 1

        # Result is the maximum water found
        return area











