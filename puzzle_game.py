### This is an CodeChef problem
# Asked in Multiple Companies like Cisco, Amazon, Facebook, Google, Microsoft etc..

#https://www.codechef.com/problems/H1
from typing import Deque
class puzzlegame:
    def solve_puzzle(self, grid):
        primes = [1,2,3,5,7,11,13,17]  # arr containing prime Numbers
        m ,n = len(grid), len(grid[0])
        
        directions = [[-1,0], [1,0], [0,-1], [0,1]]  # top, down , left and right 
        visited = set() # to keep track of visited rows and columns
        sr, sc = 0, 0
        
        q = Deque()
        q.append([sr, sc, 0])

        while q:
            cr, cc, count = q.popleft()
            if (cr == m-1 and cr== n-1):
                return  count
            for direction in directions:
                nr , nc = cr + direction[0], cc + direction[1]
                if 0 < nr < m and 0< nc < n and (nr, nc) not in visited:
                    if (grid[cr][cc] + grid[nr][nc]) in primes:
                        q.append([nr, nc , count+1])
                        print(q)
                        visited.add((nr,nc)) 
                        grid[cr][cc], grid[nr][nc] = grid[nr][nc], grid[cr][cc]
    
if __name__ == "__main__":
    puzzle = puzzlegame()
    board = [[7, 3, 2], 
             [4, 1, 5], 
             [6, 8, 9]] 
    print(puzzle.solve_puzzle(board))