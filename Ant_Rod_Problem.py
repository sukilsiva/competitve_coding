### This is an Leetcode problem 
### This is Asked in an Interview of Microsft 1 Round
"""
Question :
input : 1, 1, 1, -1, 1, 1,-1, 1
output : 3

Explanation:  the ants with -1 will move left and ants with 1 will move rightwards if the the length of the rod is met ant 
fall off,
Likewise similarly we need to find the last ant position that will be on a rod 
So 3 nd position ant will be last ant to fall from the rod  
"""
class ant:
    def __init__(self) -> None:
        # Firstly we need to find the how many positive and Negative numbers in arr
        self.pos, self.neg = 0, 0
    def solve_problem(self, arr, length):
        for i in arr:
            if i == 1:
                self.pos += 1
            else:
                self.neg += 1
        
        # Then we need to use the Logic as follows
        # if -1 is present then it will come to the last left eg. in above problem 
        # it becomes -1 -1 1 1 1 1 1 1 Here pos > neg
        # So -1 element will fall left and 1 fall right so 2nd element will be the last to fall
        # If Neg > pos then print Negative Numbers
        # ig Both equal then print either of choice
        if self.pos > self.neg:
            return self.neg + 1
        elif self.neg > self.pos:
            return self.neg
        else:
            return self.pos or self.neg

if __name__ == "__main__":
    ant = ant()
    #ant1 = ant()
    N = int(input("Number of Ants in the rod"))
    length = N+1
    arr = []
    for i in range(0, N):
        arr.append(int(input()))
    print(ant.solve_problem(arr, length))
    #print(ant1.solve_problem(arr1, length1))