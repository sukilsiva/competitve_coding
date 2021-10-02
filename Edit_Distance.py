def solution(string1, string2, m, n):
    dp = [[0 for j in range(n+1)] for i in range(m+1)]
    
    for i in range(m+1):
        for j in range(n+1):
            if i==0: dp[i][j] = j  
            elif j==0: dp[i][j] = i
            else:    
                if string1[i-1] == string2[j-1]:
                    dp[i][j] == dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])        
    return dp 
    
if __name__ == "__main__":
    string1 = input()                   #abcmno
    string2 = input()                   #adcnestring1, string2 = string1, string2
    print(solution(string1, string2, len(string1), len(string2)))