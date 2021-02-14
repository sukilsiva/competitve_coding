# This Code is takwn from Leetcode
# Questions :
"""
Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in 
this substring is greater than or equal to k.

Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

Constraints:

    1 <= s.length <= 104
    s consists of only lowercase English letters.
    1 <= k <= 105 """
from collections import defaultdict

class substring:
    def solve_code(self, string, k):
        arr = []
        result = defaultdict()
        for i in string:
            if i in result:
                result[i] += 1
            else:
                result[i] = 1

        for value in result:
            if result[value] >= k:
                arr.append(result[value])
        return sum(arr)

if __name__ == "__main__":
    sub = substring()
    s = "ababbc"
    k = 2
    print(sub.solve_code(s, k))






















