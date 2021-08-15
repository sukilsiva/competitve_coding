"""Given an array maximum of size atmost 20 and your goal is to remove all characters from array. So You are required to do certain operations 

1) create a variable ans = 0

2) you need to remove all the distinct characters from array. If you remove the smallest distinct element subtract x from variable add, if you remove largest element from array add variable x to add.

Note : here x is the frequency of distinct element in an array

If array has one Distinct element add frequency of that element to add variable.


Test cases 1 :

n = 5 
Array = [4,4,4,4,4]
Output = 5
Explanation : since array has 1 distinct element and its frequency is 5 

Test case 2 : 
n=8
Array=[6,4,2,6,4,6,2,2] 
Output =[-2,2,8] 

Explanation: 

Distinct element are 2,4,6

First if we remove in this order 

* 2,4,6 = -3-2+3 =-2
2 is smallest element and its frequency is 4 so -3 now array is [4,6] 
4 is smallest element frequency is 2 so -2 now array is [6] 
6 is largest element and its frequency 3 array is Empty now[]

* 6,4,2= 3+2+2 = 8
6 is the largest and frequency 3 array become [4,2]
4 is the largest and frequency 2 and array becomes [2] 
2 is the only element and frequency 3 so 3

* 2,6,4 = -3+3+2 = 2 

* 4,2,6 = 2-3+3 = 2 

So distinct elements we get were [-2, 2, 8] will be a output 

Test case 3: 
n = 3
Array = [2,1,2] 

Output : [1,3] 

Explanation : 

Distinct elements were 1,3 

* 1, 2 = -1+2 = 1 
1 smallest element and frequency 1 array becomes [2]
2 biggest element and frequency 2 array becomes []

* 2,1 = 2+1 = 3
2 largest element and frequency 2 and array is [1]
1 is the only element and frequency 1 so add 1 to variable add."""
def append(arr, option):
    res = []
    if option==1:
        res.append(arr) 
    if option==2:
        return res 

def permutation(a, l, r):
    if l==r:
        print(a)
        append(a, 1)
    else:
        for i in range(l,r+1):
            a[l], a[i] = a[i], a[l]
            permutation(a, l+1, r)
            a[l], a[i] = a[i], a[l] 

def solution(input1):
    distinct_characters = set(input1)
    size = len(distinct_characters)
    s = "".join(list(distinct_characters))
    permutations = permutation(s)
    return permutations

if __name__ == "__main__":
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    print(solution(arr))