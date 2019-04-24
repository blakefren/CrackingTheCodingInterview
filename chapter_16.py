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
    return (a,b)


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

    def get_word_freq(word):
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
            if is_between(start_2[0], start_1[0], end_2[0]) and is_between(start_2[1], start_1[1], end_2[1])
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
    # input has a tuple of tuples will let us store the board as-is as a dict key.
    
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
    elif sum([col[1] for col in col_sum]) == N or forward_diag[1] == N ro backward_diag[1] == N:
        return 'O'
    else
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
# 
# This method has O(1) runtime.

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
# This method has O(____) runtime where N=____.

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
# Description
# 
# This method has O(____) runtime where N=____.

def sixteen_fifteen():
    
    pass


# 16.16
# Description
# 
# This method has O(____) runtime where N=____.

def sixteen_sixteen():
    
    pass


# 16.17
# Description
# 
# This method has O(____) runtime where N=____.

def sixteen_seventeen():
    
    pass


# 16.18
# Description
# 
# This method has O(____) runtime where N=____.

def sixteen_eighteen():
    
    pass


# 16.19
# Description
# 
# This method has O(____) runtime where N=____.

def sixteen_nineteen():
    
    pass


# 16.20
# Description
# 
# This method has O(____) runtime where N=____.

def sixteen_twenty():
    
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
# Description
# 
# This method has O(____) runtime where N=____.

def sixteen_twentyfour():
    
    pass


# 16.25
# Description
# 
# This method has O(____) runtime where N=____.

def sixteen_twentyfive():
    
    pass


# 16.26
# Description
# 
# This method has O(____) runtime where N=____.

def sixteen_twentysix():
    
    pass


