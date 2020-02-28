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
# Given an array filled with letters and numbers, find the longest subarray with an equal number of letter and numbers.
# 
# This method has O(n) runtime, where n = len(array).

def seventeen_five(array):
    
    # Assume there are no non-letter or non-number chars in the array.
    # ALso assume all letters are uppercase.

    # Build list of net letter/number counts by index.
    diff_count = [0] * len(array)
    running_count = 0
    for i in range(len(array)):
        if ord('A') <= ord(array[i]) <= ord('Z'):
            running_count += 1
        else:
            running_count -= 1
        diff_count[i] = running_count
    print(diff_count)
    
    # Find longest sequence starting and ending with the same diff.
    subarray_dict = {0:-1}
    start = 0
    end = 0
    for i in range(len(array)):
        if diff_count[i] in subarray_dict:
            if i-subarray_dict[diff_count[i]] > end-start:
                start = subarray_dict[diff_count[i]]
                end = i
        else:
            subarray_dict[diff_count[i]] = i

    return array[start+1:end+1]


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
    # We will create three queues, one for 3, 5, and 7, and take the smallest
    # number from the left side of the three. We will add multiples of that number
    # and 3, 5, or 7 to the end of the queues. We repeat this k times to get the kth number.

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
# Given an array of positive integers, find the majority element (the
# element that takes up more than half of the array). If none, return -1.
# Complete in O(n) time and O(1) space.
# 
# This method has O(n) runtime, where n = len(array).

def seventeen_ten(array):
    
    last_val = -1
    count = 0
    for i in range(len(array)):
        if count == 0:
            last_val = array[i]
        if array[i] == last_val:
            count += 1
        else:
            count -= 1
    
    if array.count(last_val) > len(array) // 2:
        return last_val
    else:
        return -1


# 17.11
# Gien a large text file of words, find the shortest distance (by
# word count) between any two words. Optimize for repeated queries.
# 
# Storing the words is O(n) runtime, where n = len(words).
# Finding the closest pair is O(w1 + w2) runtime, where w1 = number of 
# word1 in words, and w2 = number of word2 in words.

def seventeen_eleven(words, word1, word2):
    
    # words is an ordered list of the words from the file.

    # For the optimized solution, assume we would be storing this dict
    # somewhere in memory, or in a file for easy lookup.
    word_dict = {}
    for i, w in enumerate(words):
        if w not in word_dict:
            word_dict[w] = []
        word_dict[w].append(i)
    
    # Of the locations, find the shortest distance.
    # These lists are already ordered.
    word1_loc = word_dict[word1]
    word2_loc = word_dict[word2]
    shortest_distance = len(words)
    loc1 = 0
    loc2 = 0

    while loc1 < len(word1_loc) and loc2 < len(word2_loc):
        if word1_loc[loc1] > word2_loc[loc2]:
            shortest_distance = min(shortest_distance, loc1-loc2)
            loc2 += 1
        elif word2_loc[loc2] > word1_loc[loc1]:
            shortest_distance = min(shortest_distance, loc2-loc1)
            loc1 += 1
    
    return shortest_distance


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
# FInd the smallest k numbers in an array.
# 
# This method has O(n) average runtime, where n = len(array).

def seventeen_fourteen(k, array):
    
    # Edge cases.
    if k == len(array):
        return array
    if k == 0 or len(array) == 0:
        return []
    
    return quick_sort_17_14(k, array)


def quick_sort_17_14(k, array):
    
    if k == 0:
        return []

    # Set the pivot.
    pivot = randint(0, len(array)-1)
    lower = []
    same = []
    higher = []

    # Perform sort.
    for i in range(len(array)):
        if array[i] < array[pivot]:
            lower.append(array[i])
        elif array[i] == array[pivot]:
            same.append(array[i])
        elif array[i] > array[pivot]:
            higher.append(array[i])
        
    # Check for the k elements.
    if k == len(lower):
        return lower
    elif k < len(lower):
        return quick_sort_17_14(k, lower)
    elif len(lower) < k < (len(lower)+len(same)):
        return lower + same[:k-len(lower)]
    else:
        return lower + same + quick_sort_17_14(k-len(same)-len(lower), higher)


# 17.15
# Description
# 
# This method has O(____) runtime, where _ = ____.

def seventeen_sixteen():
    
    pass


# 17.16
# Given a list of back to back appointments, return the max amount of
# time that a masseuse can work given a 15 minute break between each.
# Each appt is a multiple of 15 minutes and does not overlap.
# 
# This method has O(____) runtime, where _ = ____.

def seventeen_sixteen(appointments):
    
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
