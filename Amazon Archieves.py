"""
1)
Given an array of sizes and a range m, n. Print the array as a) All elements greater than n come first.
b) All elements in range m to n come next.
c) All elements less than m appear in the end.
The order of elements in a part is in the same order of occurrence Note-Should not use additional array
Input format:
1 <= s <= Integer.MAX_VALUE
0 <= arr[i] <= Integer.MAX_VALUE
0 <= m <= Integer.MAX_VALUE 0 <= n <= Integer.MAX_VALUE
m is always less than or equal to n
Sample input 1:
S=10 arr[10] = {9, 6, 8, 3, 9, 0, 1, 5, 7,4}
m=3
n = 5
Output: (9, 6, 8, 9, 7, 3, 5, 4, 0, 1)
"""

# Soltion 1:
# Create 3 Lists by using One For Loop
S=10 
arr = [9, 6, 8, 3, 9, 0, 1, 5, 7,4]
m=3
n = 5
greater = []
ranges = []
less_than = []
# Three list were Greater (Which all elements are Greater than n), Ranges(Which all elements between m and n), less than n
for i in arr:
    if i>n:
        greater.append(i)
    elif i<=n and i>=m:
        ranges.append(i)
    else:
        less_than.append(i)
greater.extend(ranges)
greater.extend(less_than)
print(greater)
# But its not preferred as More Space its been taken 3 Spaces for array namely(greater, less_than,ranges) and not recommended in question

#Solution 2:
new_arr = []
for i in arr:
    if i>n:
        new_arr.append(i)
for i in arr:
    if i<=n and i>=m:
        new_arr.append(i)
for i in arr:
    if i<m:
        new_arr.append(i)     
print(new_arr)
# This too Not Suggested as in Question given no seperate arrays are allowed, one more disadvantage is 3 for loops + one seperate space for Array


#Solution 3: (Optimized and Correct solution)
S=10
arr = [9, 6, 8, 3, 9, 0, 1, 5, 7,4]
m=3
n = 5
count = 0
for itr, val in enumerate(arr):
    if val > n:
        arr.pop(itr)
        arr.insert(count, val)
        count+=1
for itr, val in enumerate(arr):
    if val <= n and val >= m:
        arr.pop(itr)
        arr.insert(count, val)
        count+=1
for itr, val in enumerate(arr):
    if val < m:
        arr.pop(itr)
        arr.insert(count, val)
        count+=1
print(arr)            
"""
array = [1,2,3,4,5]
array = (array[-1:]+array[:-1])
print(array)"""
