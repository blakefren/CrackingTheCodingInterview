"""
Chapter Sixteen - Moderate
"""

import sys
from collections import deque
import math


# 16.1
# Swap two numbers in place without using temporary variables.
# 
# This method has O(1) runtime.

def sixteen_one(a, b):
    
    a = a^b  # Using XOR, get bits that are different between the two numbers.
    b = a^b  # a is XOR output, so check that against b - values that differ will be swapped, which gives a.
    a = a^b  # Do the same for a.
    return a, b


# 16.2
# Find the frequency of occurrences of any given word in a book.
# What if the algorithm was run multiple times?
# 
# The class declaration has O(N) runtime where N=num words in book,
# and the method get_word_freq has O(1) runtime.

class sixteen_two:
    
    def __init__(self, book):
        
        # Book is assumed to be a list of strings, where each element is a word in the book.
        
        self._word_counts = {}  # Dict to store all word counts.
        self.book = book  # List that stores all words as strings.
        
        for word in self.book:  # Store counts of each word in book.
            w = word.lower()
            if w in self._word_counts:
                self._word_counts[w] += 1
            else:
                self._word_counts[w] = 1

    def get_word_freq(self, word):
        return self._word_counts.get(word.lower(), 0)  # Returns 0 if word not in book.


# 16.3
# Given two straight line segments (with given start/end points), 
# find their intersection point, if any.
# 
# This method has O(1) runtime.

def sixteen_three(start_1, end_1, start_2, end_2):
    
    # Assuming 2-dimensional space, start_i and end_i values are tuples of dimension 2 (x_i, y_i)
    # for line i. We'll use {y = m*x + b} to solve.
    
    def is_between(a, b, c):  # Check if b is between a and c.
        return (a <= b <= c) or (a >= b >= c)
    
    # Compute slopes and y-intercepts.
    m = (0, 0)
    b = (0, 0)
    
    try:  # First line.
        m[0] = (end_1[1] - start_1[1]) / (end_1[0] - start_1[0])
        b[0] = start_1[1] - m[0]*start_1[0]
    except ZeroDivisionError:  # Line is vertical.
        m[0] = None
        b[0] = None
        
    try:  # Second line.
        m[1] = (end_2[1] - start_2[1]) / (end_2[0] - start_2[0])
        b[1] = start_2[1] - m[1]*start_2[0]
    except ZeroDivisionError:  # Line is vertical.
        m[1] = None
        b[1] = None
    
    # Compute intersection point.
    inter_pt = (None, None)
    
    if m[0] == m[1]:  # Both lines are parallel or vertical.
        
        if b[0] == b[1] and b[0] is not None:  # Lines are the same (non-vertical).
            if is_between(start_2[0], start_1[0], end_2[0]) and is_between(start_2[1], start_1[1], end_2[1]):
                return start_1
            elif is_between(start_2[0], end_1[0], end_2[0]) and is_between(start_2[1], end_1[1], end_2[1]):
                return end_1
            else:  # Line segments do not overlap.
                return None
                
        if b[0] == b[1] and b[0] is None:  # Lines are the same (vertical).
            if is_between(start_2[1], start_1[1], end_2[1]):
                return start_1
            elif is_between(start_2[1], end_1[1], end_2[1]):
                return end_1
            else:  # Vertical segments do not overlap.
                return None
            
        else:  # Lines are not the same and will never intersect.
            return None
    
    elif m[0] is not None and m[1] is not None:  # Both are non-vertical lines.
        inter_pt[0] = (b[1] - b[0]) / (m[0] - m[1])
        inter_pt[1] = (inter_pt[0] / 2) * (m[0] + m[1]) + (1 / 2) * (b[0] + b[1])
    
    elif m[0] is None and m[1] is not None:  # Line 1 is vertical.
        inter_pt[0] = start_1[0]
        inter_pt[1] = m[1]*start_1[0] + b[1]
    
    elif m[0] is not None and m[1] is None:  # Line 2 is vertical.
        inter_pt[0] = start_2[0]
        inter_pt[1] = m[0]*start_2[0] + b[0]
    
    else:
        return None  # Catch-all.
        
    # Need to check that the point of intersection is not past the edges of the line segments.
    if start_1[1] <= inter_pt[1] <= end_1[1] and start_2[1] <= inter_pt[1] <= end_2[1]:
        if start_1[0] <= inter_pt[0] <= end_1[0] and start_2[0] <= inter_pt[0] <= end_2[0]:
            return inter_pt
    
    return None  # Lines intersect outside of their segments.


# 16.4
# Figure out if there is a winner for a game of tic-tac-toe.
# 
# This method has O(N^2) worst-case runtime where N=num rows in board.
# Best case runtime for a valid board is O(N) if someone wins the top row.

def sixteen_four(board):
    
    # This method checks to see who, if anyone, won a game of tic-tac-toe.
    # It returns None if there is no winner or the board is not square, otherwise
    # it returns the winner as 'X' or 'O'.
    
    # We could make a class that stores the values for all NxN boards in a dict and
    # reference them at runtime to get O(1) performance (after initialization). Having the board
    # input as a tuple of tuples will let us store the board as-is as a dict key.
    
    # board is a tuple of tuples of the board, where 1 is an X and
    # 0 is an O. Any other char may be used to show an empty space.
    N = len(board)
    if N == 0 or N != len(board[0]):
        return None
    
    # There are four ways of winning:
    # 1 - player has all the spots in a row
    # 2 - player has all the spots in a column
    # 3 - player has the diagonal from top left to bottom right
    # 4 - player has the diagonal from bottom left to top right
    
    col_sum = []  # One list for each column.
    forward_diag = [0, 0]  # index 0 for X, index 1 for O
    backward_diag = [0, 0]  # index 0 for X, index 1 for O
    
    for i in range(N):
        
        row_sum = [0, 0]  # index 0 for X, index 1 for 0
        col_sum.append([0, 0])  # index 0 for X, index 1 for 0
        
        for j in range(N):
            
            if board[i][j] is 1:  # X
                row_sum[0] += 1
                col_sum[i][0] += 1
            elif board[i][j] is 0:   # 0
                row_sum[1] += 1
                col_sum[i][1] += 1
            
        # Forward diagonal.
        if board[i][i] == 1:  # X
            forward_diag[0] += 1
        elif board[i][i] == 0:  # O
            forward_diag[1] += 1
        
        # Backward diagonal.
        if board[N-i-1][i] == 1:  # X
            backward_diag[0] += 1
        elif board[N-i-1][i] == 0:  # O
            backward_diag[1] += 1
            
        if row_sum[0] == N:
            return 'X'
        elif row_sum[1] == N:
            return 'O'
    
    if sum([col[0] for col in col_sum]) == N or forward_diag[0] == N or backward_diag[0] == N:
        return 'X'
    elif sum([col[1] for col in col_sum]) == N or forward_diag[1] == N or backward_diag[1] == N:
        return 'O'
    else:
        return None


# 16.5
# Find the number of trailing zeros in n factorial.
# Brute force solution - there is a more efficient way in the book.
# Other than efficiency, this solution can create numbers larger than an int type can store.
# 
# The class init and zeros method has O(N) runtime where N=N.

class sixteen_five:
    
    def __init__(self, N=100):
        self._num_zeros = {0:1, 1:0}  # Provides O(1) lookup for number of trailing zeros.
        self._factorial = {0:1, 1:1}  # Provides O(1) lookup for factorial values.
        self._max_N = N
        
        # Precompute all values up to N=100 or user-specified value.
        for i in range(1, N+1):
        
            self._factorial[i] = self._factorial[i-1] * i
            
            i_string = str(i)
            zero_count = 0
            for j in reversed(range(len(i_string))):
                if i_string[j] == '0':
                    zero_count += 1
                else:
                    break
            self._num_zeros[i] = zero_count
            
    
    def get_trailing_zeros(N):
        
        if N in self._num_zeros:
            return self._num_zeros[N]
        
        # If we have not calculated the value for N already, then do so.
        for i in range(self._max_N, N+1):
        
            self._factorial[i] = self._factorial[i-1] * i
            
            i_string = str(i)
            zero_count = 0
            for j in reversed(range(len(i_string))):
                if i_string[j] == '0':
                    zero_count += 1
                else:
                    break
            self._num_zeros[i] = zero_count 
        
        return self._num_zeros[N] 


# 16.6
# Given two arrays of integers, find the pair that has the smallest non-negative difference.
# A pair contains one value from each array.
# 
# This method has O(N*logN + M*logM) runtime where N=len(array_1) and M=len(array_2).

def sixteen_six(array_1, array_2):
    
    if len(array_1) == 0 or len(array_2) == 0:
        return None
    
    array_1.sort()  # O(N*logN)
    array_2.sort()  # O(M*logM)
    smallest_diff = sys.maxsize
    i = 0
    j = 0
    
    while i <= len(array_1) and j <= len(array_2):  # O(N+M)
        
        diff = abs(array_1[i] - array_2[j])
        if diff < smallest_diff:
            smallest_diff = diff
        
        if array_1[i] < array_2[j]:  # Need to increase i.
            i += 1
            
        elif array_1[i] > array_2[j]:
            j += 1
            
        else:
            return 0
    
    return smallest_diff


# 16.7
# Find the max of two numbers without using if/else statements or comparison operators.

def sixteen_seven(a, b):
    return (a+b)/2 + abs(a-b)/2


# 16.8
# Given any integer, print the English phrase that describes the integer.
# Ex.: 1234 = 'one thousand two hundred thirty four'
# For the sake of time, I will assume that abs(number) is less than one trillion.
# 
# This method has O(log N) runtime where N=num.

def sixteen_eight(num):
    
    if num == 0:
        return 'zero'
    
    ones = {0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
    teens = {0:'ten', 1:'eleven', 2:'twelve', 3:'thirteen', 4:'fourteen', 5:'fifteen', 6:'sixteen', 7:'seventeen', 8:'eighteen', 9:'nineteen'}
    tens = {0:'', 2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'}
    hundreds = {0:'', 1:'one hundred', 2:'two hundred', 3:'three hundred', 4:'four hundred', 5:'five hundred', 6:'six hundred', 7:'seven hundred', 8:'eight hundred', 9:'nine hundred'}
    groupings = ['thousand', 'million', 'billion']
    place_vals = [ones, tens, hundreds]
    
    output_str = []
    not_zero_count = 0
    no_int_flag = False
    str_num = str(num)
    power = len(str_num)
    
    for char in str_num:  # O(logN) loop.
        
        if char == '-':
            output_str.append('negative')
            power -= 1
            continue
        
        if char != '0':
            not_zero_count += 1
        
        new_val = place_vals[(power-1)%3].get(int(char), None)
        temp_flag = False
        if new_val is None:  # A teen number.
            new_val = teens[int(char)]
            temp_flag = True
        
        if new_val != '' and not no_int_flag:
            output_str.append(new_val)
        
        if no_int_flag:
            no_int_flag = False
        
        if temp_flag:
            no_int_flag = True
        
        if (power-1)%3 == 0:
            if power > 1 and not_zero_count > 0:
                output_str.append(groupings[power//3-1])
            not_zero_count = 0
        
        power -= 1
    
    return ' '.join(output_str)


# 16.9
# Write methods to implement multiply, subtract, and divide for integers.
# You can use the add operator, but not multiply, subtract, or divide.
# 
# This method has O(____) runtime where N=____. (INCOMPLETE)

class sixteen_nine:
    
    def __init__(self):
        pass
    
    @staticmethod
    def subtract(a, b):
        # TODO: only takes raw difference, do I need to make this order sensitive?
        # Book says to use the add operator somehow?
        return a^b
    
    @staticmethod
    def multiply(a, b):  # TODO: negative numbers
    
        total = 0
        if b > 0:
            for i in range(b):
                total += a
        else:
            for i in range(a):
                total += b
            
        return total
    
    # Integer division, no remainder.
    @staticmethod
    def divide(a, b):  # TODO: negative numbers
        counter = -1
        while a > 0:
            a += subtract(a, b)
            counter += 1
        return counter


# 16.10
# Given a list of people with birth and death years, find the year with the most
# people alive. Assume all live between 1900 and 2000.
# 
# This method has O(N+M) runtime where N=len(people) and M=num years.

def sixteen_ten(people, start_year, end_year):
    
    # Assume that people is a list of tuples of length two, where the first element in the
    #tuple is the year of birth and the second element is the year of death.
    
    year_changes = {year:0 for year in range(start_year, end_year+2)}  # O(M) initialization.
    
    for person in people:  # O(N) loop.
        year_changes[people[0]] += 1
        year_changes[people[1]+1] -= 1  # Need the plus one because the person isn't gone until the next year.
    
    sum = 0
    max_people = 0
    max_year = 0
    for year in year_changes.keys:  # O(M) loop.
        sum += year_changes[year]
        if sum > max_people:
            max_year = year
            max_people = sum
    
    return max_year


# 16.11
# You are building a diving board by placing a bunch of planks end to end. There are two lengths of
# plank. You have to use K planks of wood. Find all possible lengths of diving board.
# 
# This method has O(K) runtime where K=K.

def sixteen_eleven(K, long_len, short_len):
    
    queue = deque()  # Using deque for O(1) append performance.
    
    if K == 0:
        pass
    
    elif long_len == short_len:
        queue.append(K*long_len)
    
    else:    
        for i in range(K+1):
            queue.append((K - i)*long_len + i*short_len)
    
    return queue


# 16.12
# Description
# 
# This method has O(____) runtime where N=____.

def sixteen_twelve():
    
    pass


# 16.13
# Given two squares on a two-dimensional plane, find a line that would cut these two squares 
# in half. Assume that the top and bottom sides of the square run parallel to the X-axis.

class Square:

    def __init__(self, ll_x, ll_y, ul_x, ul_y, ur_x, ur_y, lr_x, lr_y):
        
        # Assume we have some checks here to make sure the points make a square.
        if (not_a_square):
            raise ValueError
        
        # All the X/Y coords for the points of the square.    
        self.ll_x = ll_x
        self.ll_y = ll_y
        self.ul_x = ul_x
        self.ul_y = ul_y
        self.ur_x = ur_x
        self.ur_y = ur_y
        self.lr_x = lr_x
        self.lr_y = lr_y
        
        # Get side length.
        self.side_len = math.sqrt((ll_x - ul_x)**2 + (ll_y - ul_y)**2)
        
        # Get area,
        self.area = self.line_len ** 2

def sixteen_thirteen(square_1, square_2):
    
    # square_1 and square_2 are instances of the Square class above.
    
    # Assume that the squares can be anywhere on the two-dimensional plane.
    # Problem states that they have sides parallel to the X-axis (they are not rotated).
    
    # A line dividing the square in half has to go through the midpoint. So, we can find
    # the equation of a line that goes through both midpoints.
    
    sq_1_mid_x = (square_1.ll_x + square_1.lr_x) / 2
    sq_1_mid_y = (square_1.ll_y + square_1.lr_y) / 2
    sq_2_mid_x = (square_2.ll_x + square_2.lr_x) / 2
    sq_2_mid_y = (square_2.ll_y + square_2.lr_y) / 2
    
    mid_x_equal = (sq_1_mid_x == sq_2_mid_x)
    mid_y_equal = (sq_1_mid_y == sq_2_mid_y)
    
    if (mid_x_equal and mid_y_equal):  # Squares have same midpoints.
        return ''
    
    elif mid_x_equal and not mid_y_equal:  # Squares' midpoints are vertically aligned.
        return 'X = ' + str(mid_x_equal)
    
    else:  # Nothing special.
        # Equation for a line from two points is:
        # (y-y_0) = m(x-x_0)
        # y - y_1 = (y_2 - y_1)/(x_2 - x_1) * (x - x_1)
        
        m = (sq_2_mid_y - sq_1_mid_y) / (sq_2_mid_x - sq_1_mid_x)
        return 'Y - ' + str(sq_1_mid_y) + ' = ' + str(m) + ' * (X - ' + str(sq_1_mid_x) + ')'


# 16.14
# Description
# 
# This method has O(____) runtime where N=____.

def sixteen_fourteen():
    
    pass


# 16.15
# Return the number of hits and pseudo-hits for a guess in a game of Master Mind.
# Master Mind: there are four slots, each with one color of Red/Green/Blue/Yellow.
# The player guesses four colors, and for each guess, it can either be a hit (correct
# color and space), a pseudo-hit (correct color, incorrect space), or a miss (color is
# not in the answer).
# 
# This method has O(N) runtime where N=number of slots in the guess/solution.

def sixteen_fifteen(guess, solution):
    
    # Assume that each input is a four-character string of the colors. 
    # R=Red, G=Green, B=Blue, and Y=Yellow.
    # This solution will work for N-length guesses and solutions.
    
    if len(guess) != len(solution):
        return []
    
    guess = guess.upper()
    solution = solution.upper()
    
    color_counts = {
        'R':0,
        'G':0,
        'B':0,
        'Y':0,
    }
    
    # Get a hash table of the number of each color excluding hits.
    for i, color in enumerate(solution):
        if solution[i] != guess[i]:
            color_counts[color] += 1
    
    hits = 0
    pseudo_hits = 0
    
    # Check the guess.
    for i, color in enumerate(guess):
        if guess[i] == solution[i]:  # Hit.
            hits += 1
        elif color_counts[color] > 0:  # Pseudo-hit.
            pseudo_hits += 1
            color_counts[color] -= 1
    
    return [hits, pseudo_hits]


# 16.16
# Given an array of integers, find the indeces m and n so that, if m through n were sorted,
# the entire array would be sorted. Find the smallest sub array (minimize n-m).
# 
# This method has O(N) runtime where N=len(array).

def sixteen_sixteen(array):
    
    # Find the largest number on the left at the end of a continuously increasing run, and
    # the smallest number on the right at the beginning of a continuously decreasing run.
    
    if len(array) == 0:
        return [0, 0]
    
    # Initiate vars for m.
    m = 0
    run = [array[0]]
    remaining_min = sys.maxsize
    run_flag = True
    
    # Loop through array once for m.
    for i in range(1, len(array)):
        
        if run_flag:  # Identify the continually increasing run at the start.
            
            if array[i] >= array[i-1]:
                run.append(array[i])  # O(1) append.
            
            elif array[i] < array[i-1]:
                run_flag = False
                remaining_min = min(array[i], remaining_min)
        
        else:  # Find the lowest value in the remaining array elements.
            remaining_min = min(array[i], remaining_min)
    
    if remaining_min == sys.maxsize:  # Array is already sorted.
        return [0, 0]
    
    # Find the position of the largest element in run that is less than remaining_min.
    for j in reversed(range(len(run))):  # Going backwards in case of duplicate elements.
        if run[j] <= remaining_min:
            m = j + 1
            break
    
    # Initiate vars for n.
    n = len(array)-1
    run = []
    remaining_max = -1*sys.maxsize
    run_flag = True
    
    # Loop through array once for n.
    for k in reversed(range(1, len(array))):
        
        if run_flag:  # Find the continually decreasing run at the end.
            
            if array[k] >= array[k-1]:
                run.append(array[k])  # run will be in decreasing order.
            
            elif array[k] < array[k-1]:
                run_flag = False
                remaining_max = max(array[k], remaining_max)
        
        else:  # Find the largest value in the remaining array elements.
            remaining_max = max(array[k], remaining_max)
    
    # Find the position of the smallest element in run that greater than remaining_ma
    for l in reversed(range(len(run))):  # Backwards in case of duplicate elements.
        if run[l] >= remaining_max:
            n = (len(array) - 1) - (l + 1)
            break
    
    return [m, n]


# 16.17
# Given an array of integers (positive and negative), find the continuous sequence
# with the largest sum.
# 
# This method has O(N) runtime where N=len(array).

def sixteen_seventeen(array):
    
    # We can look at a running sum through the array. 
    # If the array becomes larger than max_sum, set max_sum to it.
    # If the sum becomes negative, reset the running sum to 0.
    
    max_sum = -1*sys.maxsize
    current_sum = 0
    
    for item in array:
        
        current_sum += item
        max_sum = max(current_sum, max_sum)
        if current_sum < 0:
            current_sum = 0
            
    return max_sum


# 16.18
# Given a pattern and a value string, determine if value matches the pattern for two substrings.
# Pattern holds chars a and b and denote the pattern followed by the two substrings.
# 
# This method has O(N^2) runtime where N=len(value).

def sixteen_eighteen(pattern, value):
    
    if len(pattern) == 0 or len(value) == 0:
        return False
    
    # main is either a or b, alt is the other.
    main_char = pattern[0]
    main_count = pattern.count(main_char)  # O(N).
    alt_char = 'a' if main_char == 'b' else 'b'
    alt_count = pattern.count(alt_char)  # O(N).
    
    for main_len in range(1, len(value) // main_count + 1):  # Iterate for the main substring. O(N) loop.
        
        main_sub = value[0:main_len]  # O(N).
        alt_sub = None
        alt_len = -1
        
        # Get alt_len.
        if alt_count == 0:
            alt_len = 0
        else:
            alt_len = (len(value) - main_len * main_count) // alt_count
        
        # Get alt_sub.
        if (alt_len * alt_count) + (main_len * main_count) != len(value):
            continue  # Number of projected characters is incorrect; main_len is wrong.
        else:
            if alt_count > 0:
                first_alt_pos = pattern.index(alt_char) * main_len
                alt_sub = value[first_alt_pos:alt_len+first_alt_pos]  # O(N).
            else:
                alt_sub = ''
        
        # Build the test string.
        test_string = []
        for pattern_char in pattern:  # O(N).
            test_string.append(main_sub if pattern_char == main_char else alt_sub)
        
        # Compare the test string.
        if ''.join(test_string) == value:  # O(N) comparison.
            return True
        
    return False


# 16.19
# Given an integer matrix representing a land area where 0's are water, find
# the sizes of all ponds. A pond is one or more adjacent 0's, where adjacent is defined
# as being vertically, horizontally, or diagonally next to another 0.
# 
# This method has O(RC) runtime where R=num_rows and C=num_cols. At worst, each cell is hit 9 times.

def sixteen_nineteen(land):
    
    # pond is a list of lists, assumed to be rectangular.
    
    # We can iterate through all chars to look for zeros (water).
    # If we find one, we can recursively check all neighbors for zeros, and their neighbors, etc.
    # Once we have visited a water cell, change its value so we don't visit it again.
    
    def find_size(row, col):
        
        if 0 > row or row >= len(land) or 0 > col or col >= len(land[0]) or land[row][col] != 0:
            return 0
        
        land[row][col] = -1
        size = 1
        for r in range(-1, 2):
            for c in range(-1, 2):
                size += find_size(row+r, col+c)
        
        return size
    
    
    sizes = []    
    if len(land) == 0 or len(land[0]) == 0:
        return sizes
    
    for i, cols in enumerate(land):  # O(R) loop.
        for j in range(len(cols)):  # O(C) loop.
            if land[i][j] == 0:
                sizes.append(find_size(i, j))
    
    return sizes


# 16.20
# Given a dictionary of English words, find all words that match a number taken
# from a numeric keypad representation (cell phone keys). Ex.: 8733 -> [tree, used]
# 
# This method has O(____) runtime where N=____.

def sixteen_twenty(dictionary, numeric_word):
    
    # Store the entire English dictionary in a hash table where the key
    # is the phone number representation, and the value is the word.
    # Precalculation work is O(N) for the number of words in the English language.
    # Lookups then become O(D) for the number of digits in the word.
    
    pass


# 16.21
# Description
# 
# This method has O(____) runtime where N=____.

def sixteen_twentyone():
    
    pass


# 16.22
# Description
# 
# This method has O(____) runtime where N=____.

def sixteen_twentytwo():
    
    pass


# 16.23
# Description
# 
# This method has O(____) runtime where N=____.

def sixteen_twentythree():
    
    pass


# 16.24
# Given an array of ints and a integer value, find all array element pairs that
# sum to the given value.
# 
# This method has O(N) runtime where N=num values in array.

def sixteen_twentyfour(array, value):
    
    sum_matches = []
    array_vals = {}
    
    for num in array:  # Count occurences of numbers in array. O(N) loop.
        if num not in array_vals:
            array_vals[num] = 0
        array_vals[num] += 1
    
    for num in array:  # O(N) loop.
        needed_val = value - num
        if (num != needed_val and array_vals.get(needed_val, 0) >= 1) or (num == needed_val and array_vals.get(needed_val, 0) >= 2):  # O(1) lookup.
            sum_matches.append((num, needed_val))
            array_vals[num] -= 1
            array_vals[needed_val] -= 1
    
    return sum_matches


# 16.25
# Create a "least recently used" cache. It has a max size and will remove the least
# recently used item when inserting new elements while at the max size. The cache should map
# keys to values and return the value associated with the key when queried.
# 
# This class has O(N) runtime for insertion at max size where N=max_size, and 
# O(1) for all other operations. This can be O(1) with the book method.

import datetime

class sixteen_twentyfive:
    
    def __init__(self, max_size):
        self._max_size = max_size
        self._current_size = 0
        self._dict = {}
        self._last_use = {}
    
    def insert_value(key, value):
        
        # Remove an item if needed, otherwise increment size by one.
        if self._current_size == self._max_size:  # Remove least recently used item.
            key_to_remove = min(self._last_use, key=self._last_use.get)
            del self._dict[key_to_remove]
            del self._last_use[key_to_remove]
        else:  # Add new value or overwrite existing value.
            self._current_size += 1
        
        # Add the new item.
        self._dict[key] = value
        self._last_use[key] = datetime.datetime.now()
    
    def remove_value(key):
        try:
            if key in self._dict:
                del self._dict[key]
                del self._last_use[key]
                self._current_size -= 1
                return True
        except:
            return False
    
    def get_value(key):
        self._last_use[key] = datetime.datetime.now()
        return self._dict.get(key, None)


# 16.26
# Create a calculator for a string of basic arithmetic, including addition,
# subtraction, multiplication, and division.
# Ex.: equation = 2*3+5/6*3+15
# I am assuming there are no parenthesis and all numbers are integers.
# 
# This method has O(____) runtime where C=number of chars in equation.

# INCOMPLETE

def sixteen_twentysix(equation):
    
    # Parse through the equation and identify all numbers and operators.
    object_type = {}  # Dict where key=string_index and value=[type, object_counter]
    objects_by_num = {}  # Dict where key=object_counter and value=object.
    type_nums = {
        # Ints are type 0.
        '+':1,
        '-':2,
        '*':3,
        '/':4
    }
    object_counter = 0
    current_num = False
    
    def is_int(num):
        try:
            int(num)
            return True
        except:
            return False
    
    # Fill dicts with info.
    for i, char in enumerate(equation):  # O(C) loop.
        
        if is_int(char):
            if not current_num:  # New number after operator (or start).
                object_counter += 1
            object_type[i] = [0, object_counter]
            objects_by_num[object_counter] = objects_by_num.get(object_counter, 0)*10 + int(char)
            current_num = True
        
        else:  # Operators.
            object_counter += 1
            object_type[i] = [type_nums[char], object_counter]
            objects_by_num[object_counter] = char
            current_num = False
    
    # Iterate through the equation and run multiply and divide operations.
    for id in objects_by_num.keys():
        if objects_by_num[id] == '*':
            
