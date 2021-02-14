### Leetcode , Hackerrank and Code Chef problem almost asked in every interview
# Here we use recursion to solve the problem

"""

Given an array and a number, print all subsets with sum equal to given the sum.

Examples:

Input :  arr[] =  {2, 5, 8, 4, 6, 11}, sum = 13
Output : 
5 8
2 11
2 5 6

Input : arr[] =  {1, 5, 8, 4, 6, 11}, sum = 9
Output :
5 4
1 8

"""
class subset:
    def solve_subsets(self, arr, n, v, sum):
        # If the sum == 0 then we need to traverse through the v stores subsets
        if sum == 0:
            for value in v:
                print(value, end=" ")
            print()
        # If there is no elements remain in the array 
        if n == 0:
            return
        # Here is an actual problem first not considering the last element 
        self.solve_subsets(arr, n-1, v, sum)
        V1 = [] + v
        V1.append(arr[n-1])
        # Considering the last element from the array
        self.solve_subsets(arr, n-1, V1, sum- (arr[n-1]))
    def printsubsets(self, arr, n, sum):
        # Here using recusion for every array we are going to consider a case by accepting the last element of an array
        # and Rejecting the last element of an array
        # V is used to save the last values for considering part 
        v = []
        self.solve_subsets(arr, n, v, sum)

if __name__ == "__main__":
    arr = [2, 5, 8, 4, 6, 11]
    n = len(arr)
    sum = 13
    sub = subset()
    sub.printsubsets(arr, n, sum)