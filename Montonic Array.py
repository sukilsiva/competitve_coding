### This is an Hashcode Problem
### Link for the problem https://leetcode.com/problems/monotonic-array/
class solution:
    def case1(self, array, arr):
        prev = array[0]
        for i in range(1, len(array)):
            curr  = array[i]
            if prev <= curr:
                pass
            else:
                arr[i] = False
            prev = curr
        return arr
    def case2(self, array, arr):
        prev = array[0]
        for i in range(1, len(array)):
            curr  = array[i]
            if prev >= curr:
                pass
            else:
                arr[i] = False
            prev = curr
        return arr
    def Monotonicarray(self, array):
        prev = array[0]
        curr = array[1]
        arr = [True for j in range(len(array))]
        if prev < curr:
            answer = self.case1(array, arr)
        else:
            answer = self.case2(array, arr)

        for i in answer:
            if i == False:
                return False
        return True

if __name__ == "__main__":
    solve = solution()
    array = [1,2,2,3]
    print(solve.Monotonicarray(array))