### This is an HackerRank Problem
class bomb_diffuser:
    def diffuse(self, A, B):
        ### Creating the new array to store the Output Values
        result = []
        ### Step1: making an A Value into list of Numbers
        A = [int(i) for i in str(A)]   
        n = len(A)
        count = 0
        ### Declare Variables to Pick up first two int from list
        i = 0
        j = 1
        # To stop the loop before it reaches index Bound Error
        while count < n-1:
            num = int(str(A[i]) + str(A[j]))
            res = num * B
            ### Apppend the Value to the result array
            result.append(res)
            ### Remove the first element from the A List
            A.pop(i)
            ### Make an List into single number
            strings = [str(integer) for integer in A]
            a_string = "".join(strings)
            an_integer = int(a_string)
            count += 1
            ### Recursively do the Same Operation
            self.diffuse(an_integer, B)
        # Return the Final Output
        return result
if __name__ == "__main__":
    diffuser = bomb_diffuser()
    print(diffuser.diffuse(12345,11))
    print(diffuser.diffuse(98765,23))