"""
Chapter One - Arrays and Strings

Interview Questions
"""


# 1.1
# Determine if a string has all unique characters.
#
# This method has O(N) runtime using another data structure, where N=len(str).
# This method has O(N log N) runtime without using another data structure, where N=len(str).

def one_one(str):
    
    ''' # This solution uses another data structure.
    # If length 0 or 1, all chars are unique.
    if len(str) == 0 or len(str) == 1:
        return True
    
    # Save chars in dict one at a time, if key exists, return False.
    # "Hash" table implementation.
    # O(N) operation.
    char_dict = {}
    for char in str:
        if char in char_dict:
            return False
        else:
            char_dict[char] = True
    
    return True
    '''
    
    # This solution does not use another data structure.
    str = sorted(str)  # O(N log N) operation.
    for i in range(len(str) - 1):  # O(N) operation.
        if str[i] == str[i+1]:
            return False
    
    return True


# 1.2
# Check if one string is a permutation of another.
#
# This method has O(N) runtime, where N=len(str_one).

def one_two(str_one, str_two):
    
    # Check string, lengths, they should be the same.
    if len(str_one) != len(str_two):  # O(1) operation.
        return False
    
    # Store str_two char counts in a dict (hash table).
    str_dict = {}
    for char in str_two:  # O(N) operation.
        if char in str_dict:  # O(1) operation.
            str_dict[char] += 1
        else:
            str_dict[char] = 1
    
    # Check all str_one chars against the hash table.
    str_two = list(str_two)  # O(N) operation.
    for i in range(len(str_one)):  # O(N) operation.
        
        check_val = str_dict.get(str_one[i], -1)  # O(1) operation.
        if check_val <= 0:
            return False
        else:
            str_dict[str_one[i]] -= 1
        
    return True


# 1.3
# Replace all spaces in a string with "%20".
# The string has enough space at the end to store the extra chars.
# We are given the "True" length of the string.
# 
# This method has O(N) runtime, where N=str_length.

def one_three(input_str, str_length):
    
    input_str = list(input_str)
    index = len(input_str)  # Starting at the end.
    for i in reversed(range(str_length)):  # O(N) loop.
        
        len_to_move = 1  # Default move string 1 char.
        str_replace = input_str[i]  # Default replace with current char.
        
        if input_str[i] == ' ':  # If space, move string 3 chars and replace.
            len_to_move = 3
            str_replace = '%20'
        
        input_str[index - len_to_move: index] = str_replace
        index -= len_to_move
    
    return ''.join(input_str)


# 1.4
# Check if a string is a permutation of a palindrome.
# 
# This method has O(N) runtime, where N=len(string).

def one_four(string):
    
    # Assume input is made of alphabetical chars only.
    char_counts = [0] * 26  # Alphabet list.
    a = ord('A')
    z = ord('Z')
    
    for char in string:  # O(N) loop.
        char_val = ord(char.upper())
        if char_val >= a and char_val <= z:
            char_counts[char_val-a] += 1
    
    # Two cases for palindrome.
    # One: if all chars have even counts.
    # Two: if all chars have even counts and one char as odd count.
    odd_count = 0
    for num in char_counts:
        if num % 2 != 0:
            odd_count += 1
        if odd_count > 1:
            return False
        
    return True
    

# 1.5
# Check if two strings are one "edit" away (insert, remove, replace a single char).
# 
# This method has O(N) runtime, where N=len(longer_str).

def one_five(str_one, str_two):
    
    # We can do all checks at once (complex - difficult),
    # or figure out which check is needed, then do it.
    
    # Easy case.
    if str_one == str_two:
        return True
    
    # If diff of lengths is more than 1, they can't be only one edit away.
    if abs(len(str_one) - len(str_two)) > 1:
        return False
    
    # Check for replace.
    num_edits = 0
    if len(str_one) == len(str_two):  # O(N) loop.
    
        for i in range(len(str_one)):
            if str_one[i] != str_two[i]:
                num_edits += 1
            if num_edits > 1:
                return False
        
        return True
    
    # Check for insert/remove.
    else:
        
        j = 0
        for i in range(len(str_one)):  # O(N) loop.
            if (j+1) < len(str_two):
                if str_one[i] != str_two[j]:
                    j +=1
                    num_edits += 1
                j += 1
                if num_edits > 1:
                    return False
        
        return True


# 1.6
# Perform string compression using counts of repeated characters.
# Ex.: 'aabcccccaaa' -> a2b1c5a3
# 
# This method has O(N) runtime, where N=len(input_str).

def one_six(input_str):
    
    # Loop through string, getting char counts.
    # Also build compressed_str.
    # Ignoring case.
    input_str = input_str.lower()
    compressed_str = []  # Using a list instead of a string changes appends from O(N) best case to O(1) amortized.
    current_char = input_str[0]
    current_char_count = 1
    
    for i in range(len(input_str)):  # O(N) loop.
    
        if (i+1) < len(input_str):
            if input_str[i] == input_str[i+1]:  # Current and next char are the same.
                current_char_count += 1
            else:  # New char.
                compressed_str.append(current_char + str(current_char_count))  # O(1) amortized.
                current_char_count = 1
                current_char = input_str[i+1]
                
        else:  # Provision for last char in string.
            compressed_str.append(current_char + str(current_char_count))  # O(1) amortized.
    
    if len(compressed_str) >= len(input_str):
        return input_str
    else:
        return ''.join(compressed_str)


# 1.7
# Rotate an NxN matrix by 90 degrees, in place if possible.
# For Python, I'm assuming the input is a list of lists, all of length N.
# I'm also assuming the 90 deg rotation is clockwise.
# 
# This method has O(N^2) runtime, where N=side_length.

def one_seven(matrix):
    
    '''  # Method with extra matrix.
    # Get side length, make empty matrix.
    side_length = len(matrix)
    output_matrix = [[0 for _ in range(side_length)] for _ in range(side_length)]  # O(N^2) operation.

    for row in range(side_length):  # O(N) loop.
        for col in range(side_length):  # O(N) loop.
            
            # Convert to new coordinates.
            new_row = col
            new_col = (side_length - 1) - row
            output_matrix[new_row][new_col] = matrix[row][col]
    
    return output_matrix'''
    
    # In-place method.
    # Iterate through matrix in concentric rings.
    side_length = len(matrix)
    for row in range(side_length//2 + side_length%2):  # Loop through first half of rows, including middle.
        
        first_val = None
        for col in range(row, side_length-row-1):  # Loop through cols, including middle.
            
            # Save first value.
            first_val = matrix[row][col]
            
            # Bottom left to top left.
            matrix[row][col] = matrix[side_length-col-1][row]
            
            # Bottom right to bottom left.
            matrix[side_length-col-1][row] = matrix[side_length-row-1][side_length-col-1]
            
            # Top right to bottom right.
            matrix[side_length-row-1][side_length-col-1] = matrix[col][side_length-row-1]
            
            # Top left to top right. 
            matrix[col][side_length-row-1] = first_val
    
    return matrix


# 1.8
# For an MxN matrix, make all values zero in rows and columns that contain zeros.
# 
# This method has O(MxN) runtime, where M=num_rows and N=num_cols.

def one_eight(matrix):
    
    M = len(matrix)
    if M == 0: return matrix
    N = len(matrix[0])
    
    row_zeros = {}
    col_zeros = {}
    
    # Get all rows and cols with zeros.
    for row in range(M):  # O(M) loop.
        for col in range(N):  # O(N) loop.
            if int(matrix[row][col]) == 0:
                row_zeros[row] = True  # O(1)
                col_zeros[col] = True  # O(1)
    
    # Loop through all rows.
    for row in row_zeros:
        for col in range(N):
            matrix[row][col] = 0
            
    # Loop through all cols.
    for row in range(M):
        for col in col_zeros:
            matrix[row][col] = 0
    
    return matrix


# 1.9
# Check if one string is a rotation of another using only one call to isSubstring (Java method).
# 
# This method has O(N) runtime, where N=len(string).

def one_nine(string_one, string_two):
    
    if len(string_one) != len(string_two):
        return False
    
    string_one = string_one + string_one  # O(N) operation.
    
    if string_one.find(string_two):
        return True
    
    return False
