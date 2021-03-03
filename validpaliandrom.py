### This is an Hashcode Problem
### The Link to the problem is https://leetcode.com/problems/valid-palindrome/
class solution:
    def is_paliandrome(self, string):
        reversed = string[::-1]
        if string == reversed:
            return True
        else:
            return False

    def solve(self, string):
        string = string.lower()
        array = list(string)
        punctuations = [",", ":", " "]
        s = ""
        for i in array:
            if i in punctuations:
                pass
            else:
                s += i

        return self.is_paliandrome(s)

if __name__ == "__main__":
    solve = solution()
    s = "A man, a plan, a canal: Panama"
    print(solve.solve(s))