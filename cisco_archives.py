# This question was asked in Cisco
"""
Coffee Break Puzzle at Cisco: String Generation
https://www.hackerrank.com/contests/cisco-icode/challenges/sherlock-and-string-generation/problem
"""
from collections import defaultdict

class cisco_archives:
    def to_permute(self, arr, l, r, empty):
        # Using Binary search to find the possible permutations
        # Recursion
        # Backtracking
        if l==r:
            word = ''.join(arr)
            empty.add(word)
        else:
            for i in range(0, r+1):
                arr[l], arr[i] = arr[i], arr[l]
                self.to_permute(arr, l+1, r, empty)
                arr[l], arr[i] = arr[i], arr[l]
        return empty
    def alpha_to_word(self, array, length):
        word =""
        i=0
        # make the word accordingly to the conditions odd element should be frequency 0dd and even elements should be freq be even
        while array and len(word) < length:
            element = array[i]
            word += element * (i+1)
            element = "" #backtracking
            i += 1
        return word
            
    def string_generation(self, n, k):
        # Here in this problem n is lenght of string to be generated 
        # k is the max number of alphabets we can include 
        # (i.e) a =1 b=2 and so on .. until z=26
        # we need to return a output string if more string arises we need to output the shortest lexicolaggy string
        # here we are going to use permutations for generating possible combinations
        string = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        # Create an array to store the possible alphabets
        alphabets = []
        for i in range(0, k):
            alphabets.append(string[i])
        if len(string)!=n:
            return "String Not possible"
        else:
            # Now we need to make the possible word 
            string = self.alpha_to_word(alphabets, n)
            # Now we need to do possible permutations with the string
            array = list(string)
            possible = set()
            permutations = self.to_permute(array, 0, n-1, possible)
            # Finally sort the answer to get the shorted llexical string
            answer = sorted(permutations)
            return answer[0]

if __name__ == "__main__":
    cisco = cisco_archives()
    print(cisco.string_generation(2, 1))
    