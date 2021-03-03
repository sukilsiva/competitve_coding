### This is an Leetcode Problem
### Link : https://leetcode.com/problems/complex-number-multiplication/

class solution:
    def solve(self, a, b):
        ra, ia = a[:-1].split("+")
        rb, ib = b[:-1].split("+")

        # Convert all parts to integer.
        ra, rb = int(ra), int(rb)
        ia, ib = int(ia),int(ib)

        # Return result with formula of multiply for complex numbers.
        return "{}+{}i".format((ra*rb)-(ia*ib),(ra*ib)+(ia*rb))

if __name__ == "__main__":
    solve = solution()
    a, b = "1+-1i", "1+-1i" 
    print(solve.solve(a, b))