"""
Chapter Seventeen - Hard
"""

from random import randint
from collections import deque
import sys


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
# Generate a set of m integers from an array of size n, where each of the n! permutations
# has an equal chance of being chosen. Assume a perfect random number generator.
# 
# This method has O(n) runtime, where n = number array size.

def seventeen_three(m, numbers):

    n = len(numbers)
    if m > n:
        return []

    m_lst = numbers[0:m]

    for i in range(m, n):  # Swap numbers after m.
        index = randint(0, i)  # Assume this is a perfect generator.
        if index < m:
            m_lst[index] = numbers[i]

    return m_lst


# 17.4
# An array A contains all integers from 0 to n except for one number. Find the missing integer.
# You cannot access the entire array A with a single operation. You can access the jth bit of
# the ith number in A using an assumed method.
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
# Count the number of 2's that appear in all numbers from 0 to n.
# 
# This method has O(n*log(n)) runtime.

def seventeen_six(n):

    # Brute force solution. There is a better solution.
    num_twos = 0

    for i in range(n+1):  # To include n as well.
        num_twos += str(i).count('2')  # O(2j) where j=num digits in i, which scales with log(N).

    return num_twos


# 17.7
# Given a list of baby names and the number of babies with those names, and a list of
# name synonyms (e.g., John and Jon), find the true number of babies with those names.
# 
# This method has O(NS) runtime, where N = number of names and S = number of synonym pairs.
# This is a worst-case runtime if all names are synonyms of one another.

def seventeen_seven(names_dict, synonyms):

    # names is a dict of name:count.
    # synonyms is a list of tuples of size 2, where each tuple has two names.

    # Store the synonyms in a graph. Each connected subgraph will have all synonyms.
    edges = {}
    visited_nodes = {}
    for name in synonyms:  # O(S).

        visited_nodes[name[0]] = False
        if name[0] not in edges:
            edges[name[0]] = []
        edges[name[0]].append(name[1])

        visited_nodes[name[1]] = False
        if name[1] not in edges:
            edges[name[1]] = []
        edges[name[1]].append(name[0])

    # Perform a BFS through each subgraph to get the true name counts.
    true_counts = {}
    for name in names_dict:  # O(N).

        if visited_nodes[name]:  # Already processed this name.
            continue

        # BFS through the graph.
        true_counts[name] = 0
        queue = deque()
        queue.append(name)
        while queue:  # This and for loop are O(S) worst case together.

            # Get current node/name and increase count.
            current_name = queue.popleft()
            visited_nodes[current_name] = True
            true_counts[name] += names_dict[name_node]

            # Go through all adjacent nodes/names and add to queue if not visited.
            for name_node in edges[current_name]:
                if not visited_nodes[name_node]:
                    queue.append(name_node)

    return true_counts


# 17.8
# A human circus tower can only be created by people standing on one another, where people
# must be lighter and shorter people than the person below them. Given a list of people
# with heights and weights, find the largest tower they can make.
# 
# This method has O(P*logP) runtime, where P = number of people.

def seventeen_eight(people):

    # People is a list of tuples of length 2, where item[0] is their height, and item[1] is their weight.

    if len(people) == 0:
        return 0

    people = sorted(people, key=lambda x: x[0])  # Sort people by heights. O(P*logP).
    start = 0
    end = 0
    longest_sequence = 0

    for i in range(1, len(people)):  # O(P).
        if people[i][1] > people[i-1][1]:  # Weight check.
            end = i
        else:
            longest_sequence = end - start + 1
            start = i
            end = i

    return max(longest_sequence, end - start + 1)


# 17.9
# Find the k-th number so that the only prime factors are 3, 5, or 7.
# Book solution. Mine sucked.
# 
# This method has O(k) runtime.

def seventeen_nine(k):

    # Each of these numbers can be represented by:
    # number = 3^x * 5^y * 7^z

    if k == 1:
        return 1

    k_count = 1
    q_3 = deque()
    q_3.append(3)
    q_5 = deque()
    q_5.append(5)
    q_7 = deque()
    q_7.append(7)
    next_num = None

    while k_count < k:  # O(k).

        next_num = min(q_3[0], q_5[0], q_7[0])

        if next_num == q_3[0]:
            q_3.popleft()
            q_3.append(next_num * 3)
            q_5.append(next_num * 5)
            q_7.append(next_num * 7)

        elif next_num == q_5[0]:
            q_5.popleft()
            q_5.append(next_num * 5)
            q_7.append(next_num * 7)

        elif next_num == q_7[0]:
            q_7.append(next_num * 7)
            q_7.popleft()

        k_count += 1

    return next_num


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
