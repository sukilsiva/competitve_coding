class suduko_solver:
    def find_next_empty(self,puzzle):
        # Here we need to traverse through all the columns and rows of matrix 
        for r in range(9):
            for c in range(9):
                if puzzle[r][c] == -1:
                    return r, c
        # Else return the No Values
        return None, None
    def is_valid(self, puzzle, guess, row, col):
        # Here we need to check whether the guess lies in the same row or Column or within that 3*3 rows
        #step 1: Whether the guess lies in row Values
        row_vals = puzzle[row]
        if guess in row_vals:
            return False
        
        #step2: if Guess in col vals return false
        # this is tricky as every row col val changes
        # so lets  do an list comprehension
        col_vals = [puzzle [i][col] for i in range(9)]
        if guess in col_vals:
            return False

        #Step3: Lets check for an 3*3 part
        row_start =  (row //3) * 3      # as is get 3 rows
        col_start = (col // 3) * 3      # as it has 3 columns
        # Iterating through 3*3 Matrix and Find the guess is valid or Not
        # Step 3.1 If we get the all cases passes we need to return True
        for r in range(row_start, row_start +3):
            for c in range(col_start, col_start + 3):
                if puzzle[r][c] == guess:
                    return False
        
        ### Step4 : if everythng is passes
        return True
    def solve_suduko(self, puzzle):
        # Solving the suduko using Backtracking Technique
        # Mutates the Puzzle lists and return Possible Solution

        # step 1: Find the empty spaces in the Puzzle that is -1
        row, col = self.find_next_empty(puzzle)

        # Step 1.1 If there is no empty places as we alllow ony valid inputs return True
        if row is None:
            return True
            
        # Step2:  If there is a Place to put a number in puzzle we need to find the guess between (Eg. 0 to 10)
        for guess in range(1,10):
            #step3: to find valid guess
            if self.is_valid(puzzle, guess, row, col):
                # if the guess is valid then place the guess in that row and column
                puzzle[row][col] = guess

                # Now we need to do this thing recursively to solve the whole idea 
                if self.solve_suduko(puzzle):
                    return True
            #step 4: If this Guess is Wrong we need to back track
            puzzle[row][col] = -1 # Reset the puzzle
         # step 5: if the whole puzzle is Wrong return that Puzzle is Not Solvable
        return False
if __name__ == '__main__':
    example_board = [
        [-1, 7, -1,    6, -1, 2,   -1, 4, -1],
        [5, -1, -1,   -1, 1, -1,   -1, -1, 8],
        [-1, -1, -1,   -1,-1,-1,   -1,-1, -1],

        [-1,-1, -1,   -1, 9, -1,   -1, -1, -1],
        [1, 9, -1,   -1, 5, -1,   -1, 8, 3],
        [-1, -1, 4,   7, -1, 8,    6, -1, -1],

        [-1, -1, 8,   9, -1, 4,   2, -1, -1],
        [-1, -1, -1,   1, -1, -1,   -1, -1, -1],
        [-1, 3, 9,   -1, -1, -1,   1, 6, -1]
    ]

    suduko = suduko_solver()
    print(suduko.solve_suduko(example_board))
    print (example_board)
