### This is an Leetcode Problem
class minimumpath:
    def MinPath(self, grid):
        ### First of all we need to find the path to be reached
        m , n = len(grid), len(grid[0])
        destination = grid[0][0]
        for i in range(0,m):
            for j in range(0,n):
                if grid[i][j] == destination:
                    row_to_reach, column_to_reach = i, j
        ### We need to define the NUmber of rows and Columns and Create Matrix with 0 values
        minpathmatrix = [[0 for x in range(0,m)] for y in range(0, n)]
        minpathmatrix[0][0] = grid [0][0]

        ### This will set the cost values of empty matrix for rows and columns at both 0 index
        for i in range(1, m):
            abovecost = minpathmatrix[i-1][0] 
            minpathmatrix[i][0] = abovecost + grid[i][0]
        
        for j in range(1, n):
            leftcost = minpathmatrix[0][j-1]
            minpathmatrix[0][j] = leftcost + grid[0][j]
        
        ### we need to fill the empty matrx for remaining columns
        for i in range(1,m):
            for j in range(1, n):
                abovecost = minpathmatrix[i-1][j]
                leftcost = minpathmatrix[i][j-1]
                diagonalcost = minpathmatrix[i-1][j-1]

                minpathmatrix[i][j] = grid[i][j] + min(abovecost, leftcost, diagonalcost)
        
        return minpathmatrix[row_to_reach][column_to_reach]
        

if __name__ == '__main__':
    pathcost = minimumpath()
    print(pathcost.MinPath(grid = [[2,3,4],[5,9,8],[7,2,1]]))
