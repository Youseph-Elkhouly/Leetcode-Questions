class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        '''
        given a list of lists
        M x N int matrix 

        properties:

        1. each row is sorted in non decreasing order

        2. the first int of row is > than the last int of the previous row

        '''


        '''
        Psuedo code

        Left pointer = index of first element 0

        Right pointer = index of the last element (len(array - 1))



        '''



        from typing import List
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, (rows * cols) - 1

        while left <= right:
            mid = (left + right) // 2
            # convert mid (1D index) into (row, col)
            row = mid // cols
            col = mid % cols
            mid_value = matrix[row][col]

            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
