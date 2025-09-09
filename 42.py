class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        left = 0 
        right = len(height) - 1

        max_left = height[left]
        max_right = height[right]

        total_water = 0


        while left < right:
            if height[left] < height[right]:

                max_left = max(height[left], max_left)
                total_water+=max_left-height[left]

                left+=1

            else:
                max_right = max(height[right], max_right)
                total_water += max_right - height[right]
                right -= 1

        return total_water
