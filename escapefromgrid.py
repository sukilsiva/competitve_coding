### This is an HackerRank Problem 
# For reference visit the URL : https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/practice-problems/algorithm/escape-from-grid-google-ff752cb1/

from typing import Deque
class escape:
    def find_human(self, grid, M, N):
        for i in range(0,M):
            for j in range(0,N):
                if grid[i][j] == 2:
                    return i,j
    def solve_grid(self, grid):
        m ,n = len(grid), len(grid[0])
        # which direction persion to Move from current cell
        directions = [[-1,0], [1,0], [0,-1], [0,1]] # i.e Top, Down, Left, Right
        # Firstly we need to find the Human in the grid i.e 2
        hr, hc = self.find_human(grid, m,n)
        # create a set named Visited so it doesn't allows duplicated meant by visited cells
        visited = set()
        # Intitalize queue as we need to use the BFS 
        q = Deque()
        q.append([hr,hc,0]) # Current row, column and distance from human

        while q:
            cr,cc,cdist = q.popleft()
            # if Edges are reached
            if (cr == 0 or cr == (m - 1) or cc == 0 or cc == (n - 1)):
                return ("The Minimum Number of steps required is {}".format(cdist))
            # If Obstacle is found
            if grid[cr][cc] == 1:
                continue
            # Traversing through the Directions
            # Moving through each cell in a grid
            # (i.e) 0 if way is found we need to add nr , nc , cdist+1 to the queue
            for direction in directions:
                nr , nc = cr + direction[0], cr + direction[1]
                if 0 < nr < m and 0 < nc < n and (nr, nc) not in visited:
                    q.append([nr,nc, cdist+1])
                    visited.add((nr, nc))
        return "Solution Doesn't Exists"

if __name__ == "__main__":
    sample_grid = [[1,1,1,0,1],
                   [1,0,2,0,1],
                   [0,0,1,0,1],
                   [1,0,1,1,0]]
    grid_escape = escape()
    print(grid_escape.solve_grid(grid=sample_grid))