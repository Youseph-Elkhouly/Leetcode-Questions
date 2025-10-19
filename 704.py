class Solution:
    def search(self, nums: List[int], target: int) -> int:
        


        '''

        array of int = nums (Sorted in ascending order)
        int = target
        
        goal: write a function to search target in nums and 
        if target exists then return its index
        else return - 1


        time constraint: O(log n)


        Binary search review: 
        begins with 2 points one at left and one and right

        finds middle index (left + right) // 2

        compare the middle element with target if found returns 

        if smaller searches left if greater searches right

        '''



        

        length = len(nums)  #length of the input array

        lp = 0                # left pointer starts at index 0
        rp = length - 1       # right pointer starts at last index



        # keep searching while range is valid
        while lp <= rp:
            # find middle index
            mid = (lp + rp) // 2

            # check if we found the target
            if nums[mid] == target:
                return mid

            # if target is smaller, move right pointer left
            elif nums[mid] > target:
                rp = mid - 1

            # if target is larger, move left pointer right
            else:
                lp = mid + 1

        # not found
        return -1 









