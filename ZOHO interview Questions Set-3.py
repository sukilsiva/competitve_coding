### These are all random ZOHO Interview Questions taken randomly

"""
Question 1: Print all distinct permutations of a given string with duplicate characters. 

Question 2: Write a program to give the following output for the given input
Eg 1: Input: a1b10
      Output: abbbbbbbbbb
Eg: 2: Input: b3c6d15
       Output: bbbccccccddddddddddddddd
The number varies from 1 to 99.
"""

class ZOHO_COMPETETIVE_CODING:
    def toString(self,List): 
        return ''.join(List) 
    # Function to print permutations of string 
    # This function takes three parameters: 
    # 1. String 
    # 2. Starting index of the string 
    # 3. Ending index of the string. 
    def permute(self, a, l, r): 
        if l==r: 
            print (self.toString(a)) 
        else: 
            for i in range(l,r+1): 
                a[l], a[i] = a[i], a[l] 
                self.permute(a, l+1, r) 
                a[l], a[i] = a[i], a[l] # backtrack 
        
if __name__ == "__main__":
    z = ZOHO_COMPETETIVE_CODING()
    string = "ABC"
    n = len(string) 
    a = list(string) 
    z.permute(a, 0, n-1)

