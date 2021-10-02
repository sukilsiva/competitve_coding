""" Inputs from the Console:
    n : 3 no of students
    1 0 5 space seperated integers given in a line indicating no. of books each person having
    n : 4 
    1 1 5 1 
"""
def solution(n, arr):
    ### Find the Max number in a arr
    ### in our case its 5
    max_sum = max(arr)
    ### find what each element in array needed to have here its 2 [2,2,2]
    each_element_value = sum(arr)//len(arr) 
    ### Note the index of person having highest no of books
    idx = arr.index(max_sum) 
    ### form two arrays left side highest element and right side of highest element 
    ### Eg. if 4 persons are there having following respective books 1 1 5 1 
    ### then splitting as follows
    ### left side [1,1,4] and right side [3,1]
    ### count actual no of books needed 
    ### Eg. left side of 5 [1,1] 2 needed so it can be calculated by len of left side * 2 - each_element need to have
    left_side_actual = len(arr[0:idx])*each_element_value
    right_side_actual = len(arr[idx+1:n])*each_element_value
    ### Forming the arra left side and right side [1,1] and [1]
    left_side_arr = arr[0:idx]
    right_side_arr = arr[idx+1:n] 
    ### Finding the sum for both sides 2 for left side and 1 for right side 
    left_side_sum = sum(left_side_arr)
    right_side_sum = sum(right_side_arr)
    ### From below step we can find the needed 
    left_side_needed = left_side_actual - left_side_sum
    right_side_needed = right_side_actual - right_side_sum 
    left_side_arr.append(each_element_value + left_side_needed)
    right_side_arr.insert(0, each_element_value + right_side_needed)
    left_side_arr = left_side_arr[::-1]
    i,j =0,0
    l_count, r_count = 0,0
    ### from the highest books person find out the diff between books they are having
    ### and actual no of books they can have and add diff to count 
    ### for left side we will get 3 and right side 1 in above explained scenario
    while i<len(left_side_arr):
        diff_1 = left_side_arr[i] - each_element_value
        if diff_1 == 0:
            pass 
        else:
            left_side_arr[i+1] += diff_1
        l_count += diff_1 
        i+=1
    while j<len(right_side_arr):
        diff_2 = right_side_arr[j] - each_element_value 
        if diff_2 == 0:
            pass 
        else:
            right_side_arr[j+1] += diff_2
        r_count += diff_2 
        j+=1
    ### add the final count and return 
    return l_count + r_count
    ### Future scope we can use Binary search to reduce time complexity but it won't work worst case scenarios

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(solution(n,arr))
