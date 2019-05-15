"""
Chapter Ten - Sorting and Searching
"""


# 10.1
# You are given two sorted arrays, A and B, where A has a large enough buffer to
# store B at the end. Merge B into A in sorted order.
# 
# This method has O(a) runtime where a=len(A).

def ten_one(A, B):
    # We will iterate through both arrays in reverse order.

    # Assume that A and B are filled with objects that support simple comparisons.
    # Also assume that the empty elements of A are None.

    if len(B) == 0:
        return A
    if len(A) == len(B):
        for i in range(len(B)):
            A[i] = B[i]
        return A

    k = len(B) - 1  # Used to iterate through B.
    none_pos = len(A) - len(B) - 1

    for i in reversed(range(len(A))):

        print(A, i, k)  # TEMP
        if none_pos >= 0:
            if A[i] is None:
                A[i] = A[none_pos]
                A[none_pos] = None
        else:  # We have gone through all elements of A.
            A[i] = B[k]
            k -= 1
            continue

        print(A, i, k)  # TEMP
        if A[i] < B[k]:
            A[i - 1] = A[i]
            A[i] = B[k]
            k -= 1
        else:
            none_pos -= 1

        print(A, i, k)  # TEMP
        print()  # TEMP

        if k == -1:
            break

    return A


# 10.2
# Sort an array of strings so that the anagrams are next to each other.
# 
# This method has O(S) runtime where S=len(strings).

def get_string_score(string):
    print(string)
    sum = 0
    for char in string:
        sum += ord(char)
    return sum

def ten_two(strings):

    # If I give each string an integer score that is the sum of its characters in ASCII numbers, then
    # strings that are anagrams should have the same score. I can then radix sort by the score.

    str_locations = {}  # old_index:score
    sorted_str = []
    max_score = 0

    # Get the ASCII-based score for each string.
    for i in range(len(strings)):
        score = get_string_score(strings[i])
        sorted_str.append(i)
        str_locations[i] = score
        max_score = max(score, max_score)

    # Do the radix sort.
    for exp in range(len(str(max_score))):  # To loop through each digit.

        # Based this on/copied this from https://www.geeksforgeeks.org/radix-sort/.

        output = [None] * len(sorted_str)
        count = [0] * 10

        for i in range(len(sorted_str)):  # Get counts of each digit.
            index = str_locations[sorted_str[i]] // exp
            count[index % 10] += 1

        for i in range(1, 10):  # Fix counts to represent array indexes.
            count[i] += count[i - 1]

        i = 0
        while i >= 0:  # Insert values to output array in new positions.
            index = str_locations[sorted_str[i]] // exp
            output[count[index % 10] - 1] = sorted_str[i]

        for i in range(len(sorted_str)):
            sorted_str[i] = output[i]

    # Reassign the strings in their new locations.
    for i in range(len(strings)):
        sorted_str[i] = strings[sorted_str[i]]

    return sorted_str


# 10.3
# Description
# 
# This method has O() runtime where N=____.

def ten_three():
    
    pass


# 10.4
# Description
# 
# This method has O() runtime where N=____.

def ten_four():
    
    pass


# 10.5
# Description
# 
# This method has O() runtime where N=____.

def ten_five():
    
    pass


# 10.6
# Description
# 
# This method has O() runtime where N=____.

def ten_six():
    
    pass


# 10.7
# Description
# 
# This method has O() runtime where N=____.

def ten_seven():
    
    pass


# 10.8
# Description
# 
# This method has O() runtime where N=____.

def ten_eight():
    
    pass


# 10.9
# Description
# 
# This method has O() runtime where N=____.

def ten_nine():
    
    pass


# 10.10
# Description
# 
# This method has O() runtime where N=____.

def ten_ten():
    
    pass


# 10.11
# Description
# 
# This method has O() runtime where N=____.

def ten_eleven():
    
    pass
