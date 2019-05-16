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
# This method has O(S*L) runtime where S=number of strings and L=average string length.

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
    for i in range(len(strings)):  # O(S).
        score = get_string_score(strings[i])  # O(L).
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
# Given an array that has been sorted in increasing order, then rotated an unknown number of
# times, find a specific element in the array and return its index.
# 
# This method has O(logN) normal and O(N) worst-case runtime where
# N=number of array elements.

def modified_binary_search(array, element, start, end):

    middle = (end - start) // 2

    # There are a few cases that determine where we will search.

    # Search to the right - normal order.
    if array[middle] < array[end]:
        if array[middle] <= element <= array[end]:  # Right half.
            return modified_binary_search(array, element, middle + 1, end)
        else:  # Left half.
            return modified_binary_search(array, element, start, middle - 1)

    # Search to the left - normal order.
    elif array[start] < array[middle]:
        if array[start] <= element <= array[middle]:  # Left half.
            return modified_binary_search(array, element, start, middle - 1)
        else:  # Right half.
            return modified_binary_search(array, element, middle + 1, end)

    else:  # We have a lot of duplicates.

        # It should be in the right half.
        if array[start] == array[middle]:
            return modified_binary_search(array, element, middle + 1, end)

        # It should be in the left half.
        if array[middle] == array[end]:
            return modified_binary_search(array, element, start, middle - 1)

        # Could be anywhere, so search through all elements.
        else:
            for i in range(len(array)):
                if array[i] == element:
                    return i
            return -1


def ten_three(array, element):
    
    # We can do this with a modified binary search.

    if len(array) == 0:
        return None

    return modified_binary_search(array, element, 0, len(array) - 1)


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
# Given an MxN matrix where each row and column is sorted in ascending order, find an element.
# 
# This method has O(logM+logN) runtime where M=number of matrix rows and N=number of matrix columns.
# INCOMPLETE

def binary_search_matrix(matrix, element, top_row, bottom_row, left_col, right_col):

    if top_row > bottom_row:
        return -1

    middle_row = (bottom_row - top_row) // 2
    middle_col = (right_col - left_col) // 2

    if matrix[middle_row][middle_col] == element:  # Found it.
        return middle_row, middle_col

    elif element < matrix[middle_row][middle_col]:  # Search up and to the left.
        return binary_search_matrix(array, element, top_row, middle_row, left_col, middle_col)

    elif element > array[middle_row]:  # Search down and to the right.
        return binary_search_matrix(array, element, middle_row, bottom_row, middle_col, right_col)

    # TODO
    elif ____:  # Search up and to the right.
        return binary_search_matrix(array, element, top_row, middle_row, middle_col, right_col)

    elif ____:  # Search down and to the left.
        return binary_search_matrix(array, element, middle_row, bottom_row, left_col, middle_col)

    else:  # It's not here.
        return -1


def ten_nine(matrix, element):

    # I imagine some sort of binary search would be useful here.

    m = len(matrix)
    if m == 0:
        return -1, -1

    n = len(matrix[0])
    if n == 0:
        return -1, -1

    return binary_search_matrix(matrix, element, 0, m, 0, n)


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
