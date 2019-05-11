"""
Chapter Seventeen - Hard
"""


# 17.1
# Add two numbers without using any arithmetic operators.
# 
# This method has O(1) runtime.

def seventeen_one(a, b):

    # This methods works for positive integers only.
    # 1 - take XOR of two nums as c - this gives the sum w/o carrying any digits
    # 2 - take AND of two nums as d and bit shift left once - this gives the overflow digits
    # 3 - repeat 1&2 with c and d until d == 0 (no digits left to carry)

    while True:

        c = a ^ b
        d = (a & b) << 1
        e = c ^ d

        if d == 0:
            return e
        else:
            a = c
            b = d


# 17.2
# Shuffle a deck of cards. It must be a perfect shuffle, where each of the 52! permutations
# has an equal chance of being chosen. Assume a perfect random number generator.
# 
# This method has O(C) runtime where C is the number of cards in the deck.

from random import randint

def seventeen_two(cards):

    # Swap card at i with a random card in the deck.
    num_cards = len(cards)
    for i in range(num_cards):
        index = randint(0, i)
        temp = cards[index]
        cards[index] = cards[i]
        cards[i] = temp

    return cards


# 17.3
# Description
# 
# This method has O() runtime, where _ = ____.

def seventeen_three():
    
    pass


# 17.4
# Description
# 
# This method has O() runtime, where _ = ____.

def seventeen_four():
    
    pass


# 17.5
# Description
# 
# This method has O() runtime, where _ = ____.

def seventeen_five():
    
    pass


# 17.6
# Description
# 
# This method has O() runtime, where _ = ____.

def seventeen_six():
    
    pass


# 17.7
# Description
# 
# This method has O(____) runtime, where _ = ____.

def seventeen_seven():
    
    pass


# 17.8
# Description
# 
# This method has O(____) runtime, where _ = ____.

def seventeen_eight():
    
    pass


# 17.9
# Description
# 
# This method has O(____) runtime, where _ = ____.

def seventeen_nine():
    
    pass


# 17.10
# Description
# 
# This method has O(____) runtime, where _ = ____.

def seventeen_ten():
    
    pass


# 17.11
# Description
# 
# This method has O(____) runtime, where _ = ____.

def seventeen_eleven():
    
    pass


# 17.12
# Description
# 
# This method has O(____) runtime, where _ = ____.

def seventeen_twelve():
    
    pass


# 17.13
# Description
# 
# This method has O(____) runtime, where _ = ____.

def seventeen_thirteen():
    
    pass


# 17.14
# Description
# 
# This method has O(____) runtime, where _ = ____.

def seventeen_fourteen():
    
    pass


# 17.15
# Description
# 
# This method has O(____) runtime, where _ = ____.

def seventeen_fifteen():
    
    pass


# 17.16
# Description
# 
# This method has O(____) runtime, where _ = ____.

def seventeen_sixteen():
    
    pass


# 17.17
# Description
# 
# This method has O(____) runtime, where _ = ____.

def seventeen_seventeen():
    
    pass


# 17.18
# Description
# 
# This method has O(____) runtime, where _ = ____.

def seventeen_eighteen():
    
    pass


# 17.19
# Description
# 
# This method has O(____) runtime, where _ = ____.

def seventeen_nineteen():
    
    pass


# 17.20
# Description
# 
# This method has O(____) runtime, where _ = ____.

def seventeen_twenty():
    
    pass


# 17.21
# Description
# 
# This method has O(____) runtime, where _ = ____.

def seventeen_twentyone():
    
    pass


# 17.22
# Description
# 
# This method has O(____) runtime, where _ = ____.

def seventeen_twentytwo():
    
    pass


# 17.23
# Description
# 
# This method has O(____) runtime, where _ = ____.

def seventeen_twentythree():
    
    pass


# 17.24
# Description
# 
# This method has O(____) runtime, where _ = ____.

def seventeen_twentyfour():
    
    pass


# 17.25
# Description
# 
# This method has O(____) runtime, where _ = ____.

def seventeen_twentyfive():
    
    pass


# 17.26
# Description
# 
# This method has O(____) runtime, where _ = ____.

def seventeen_twentysix():
    
    pass
