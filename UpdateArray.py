### This is an Hackerrank Problem asked in amdocs Interview 

class Hackerank:
    def solution(self, arr, n):
        # Lets use an Binary search format to find the solution for low time complexity
        # find the mid element 
        # multiply n with mid element and compare with sum 
        # Compare with sum of arr and update the Mid element accordingly
        mid = n // 2
        ans = []
        while mid < n:
            mul = arr[mid] * n
            sums = sum(arr)
            if mul <= sums:
                mid += 1
            else:
                ans.append(arr[mid])
                break
        return ans[0]

if __name__ == "__main__":
    N = int(input())
    arr = [int(i) for i in input().split()]
    solve = Hackerank()
    print(solve.solution(arr, N))