"""
Chapter Five - Bit Manipulation

Python binary numbers are represented by:    0b
Numbers can be changed to binary by using:    bin(number)
Can get number of bits in number by:    len(bin(number))-2
Python bit shifters (>> and <<) are logical, not arithmetic.
"""


# 5.1
# Given two 32-bit numbers (N/M) and two bit positions (i/j), insert M into N such
# that M starts at j and ends at i. Assume that j through i have enough space to fit M.
# 
# This method has O(j) runtime where N=j.

def five_one(M, N, i, j):
    
    # Get a mask to clear bits in N from j to i.
    mask = 0
    for k in range(j-i):  # Get the right number of 1's.
        mask = mask ^ (1 << k)
    for k in range(i):  # Bit shift the mask.
        mask = mask << 1
    
    # Apply the mask to N.
    N = N & ~mask
    
    # Fill in N with M.
    N = N | (M<<i)
    
    return N


# 5.2
# Given a real number between 0 and 1 passed as a double, print the binary representation
# if at most 32 characters. Otherwise, print "ERROR".
# 
# This method has O(____) runtime where N=____.

def five_two():
    
    pass


# 5.3
# Given an integer, return the longest number of 1's that can be created by 
# flipping only one bit.
# 
# This method has O(N) runtime where N=number of bits in num.

def five_three(num):
    
    current_count = 0
    last_count = 0
    longest_count = 0
    
    for i in range(2, len(num)):
        
        # If bit is zero, increase counts.
        if num[i] == '0':
            longest_count = max(current_count + last_count + 1, longest_count)
            last_count = current_count
            current_count = 0
        
        # If bit is one, increase the count.
        else:
            current_count += 1
            longest_count = max(current_count + last_count, longest_count)
        
    
    return longest_count


# 5.4
# Description
# 
# This method has O(____) runtime where N=____.

def five_four():
    
    pass


# 5.5
# Explain what the following code does:
# ((n & (n-1)) == 0)
# 
# This method has O(b) runtime, where b is the number of bits in n.

def five_five(n):
    
    """
    This checks if n is a power of 2 (or 0).
    This is because the only way that n and (n-1) have none of the same bits (the
    & check) is when n is a power of 2, or 0.
    """
    
    return ((n & (n-1)) == 0)


# 5.6
# Description
# 
# This method has O(____) runtime where N=____.

def five_six():
    
    pass


# 5.7
# Description
# 
# This method has O(____) runtime where N=____.

def five_seven():
    
    pass


# 5.8
# Description
# 
# This method has O(____) runtime where N=____.

def five_eight():
    
    pass
