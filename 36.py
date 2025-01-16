class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

       #we can use some sort of backtracking algortihm in order to come up with a brute force solution.


        #first we can setup some sort of function to identify empty cells

        def findEmpty():
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        return row, col #which is empty
            return None #no empty cells 

        def solve():
            empty = findEmpty()
            if not empty:
                    return True
 
            row, col = empty

            for num in range(1,10):
                
                if isValid(row, col, str(num)):    
                    board[row][col] = str(num)  #this places the number

                    if solve():  #recursive call  
                        return True

                    board[row][col] = "."    #undo the move

            return False
                


        def isValid(row, col, num, board):
            # Check row
            for j in range(9):
                if board[row][j] == num and j != col:
                    return False

            # Check column
            for i in range(9):
                if board[i][col] == num and i != row:
                    return False

            # Check 3x3 sub-box
            box_row_start = (row // 3) * 3
            box_col_start = (col // 3) * 3
            for i in range(box_row_start, box_row_start + 3):
                for j in range(box_col_start, box_col_start + 3):
                    if board[i][j] == num and (i, j) != (row, col):
                        return False

            return True

        # Iterate through the board and validate each non-empty cell
        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    if not isValid(row, col, board[row][col], board):
                        return False

        return True
