"""
Chapter Two - Linked Lists
"""

# Creating a simple node class to be used in examples.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Build a linked list from a list for testing.
def llist_from_list(lst):
    
    if len(lst) == 0:
        return None
    
    n = Node(lst.pop(0))
    head = n
    
    for item in lst:
        new_node = Node(item)
        n.next = new_node
        new_node.prev = n
        n = new_node
    
    return head


# 2.1
# Remove duplicates from an unsorted linked list.
# I'm assuming this is a singly linked list whose node data includes a single integer.
#
# This method has O(N) runtime when using a hash table, where N=num_nodes.
# This method has a little less than O(N^2) runtime when not using an additional data structure, where N=num_nodes.

def two_one(head):
    
    '''
    # This version uses a hash table (dict) to store seen values.
    n = head
    found_data = {n.data:True}
    
    while n.next is not None:  # O(N) loop through all nodes.
        
        # Look ahead until we find a new data value.
        temp_node = n.next
        while temp_node.data in found_data:
            temp_node = temp_node.next
            if temp_node is None:
                break
        
        n.next = temp_node  # Leapfrog sequential duplicate node(s).
        found_data[n.next.data] = True
        
        # Move to next node.
        n = n.next
        if n is None:
            break
    
    return head'''
    
    
    # This version does not use an additional data structure.
    n_1 = head
    while n_1 is not None:  # O(N) loop.
        
        n_2 = n_1
        while n_2 is not None:  # O(N) loop.
            
            if n_2.next is None:
                break
            while n_2.next.data == n_1.data:  # Leapfrog duplicate nodes.
                n_2.next = n_2.next.next
            n_2 = n_2.next
        
        n_1 = n_1.next
    
    return head


# 2.2
# Find the kth to last element in a linked list.
# I'm assuming this is for a singly linked list, else it wouldn't be as hard.
#
# This method has O(N) runtime, where N=num_nodes.

def two_two(head, k):
    
    if k == 0:
        return None
        
    n = head
    return_node = head
    counter = 0
    while n is not None:  # O(N) loop.
        
        if counter == k:
            return_node = return_node.next
        else:
            counter += 1
        n = n.next
        
    return return_node


# 2.3
# Delete a node in the middle of a singly linked list, given access to only that node.
#
# This method has O(1) runtime.

def two_three(node):
    
    node.data = node.next.data
    node.next = node.next.next


# 2.4
# Partition a linked list around a value X such that all nodes
# less than X come before nodes greater than or equal to X.
# Neither partition needs to be sorted, and nodes equaling X
# do not need to be between the partitions.
#
# This method has O(N) runtime, where N=num_nodes.

def two_four(head, X):
    
    n = head
    less_head = None
    less_n = None
    greater_head = None
    greater_n = None
    
    while n is not None:  # O(N) loop.
        
        if n.data < X:
            if less_head is None:
                less_head = n
                less_n = n
            else:
                less_n.next = n
                less_n = n
        
        else:
            if greater_head is None:
                greater_head = n
                greater_n = n
            else:
                greater_n.next = n
                greater_n = n
        
        if n.next is None:
            break
        n = n.next
    
    less_n.next = greater_head  # Connect the two lists.
    greater_n.next = None  # Set last node to None.
    
    return less_head
    

# 2.5
# Given two linked lists, suppose the data in each represents a number with the nodes
# representing the number in reverse order. Return a new linked list that has the
# sum of these numbers, also in reverse order.
#
# This method has O(N) runtime, where N=num_nodes in the larger linked list.

def two_five(ll_1, ll_2):
    
    # To implement in the opposite order (the book's follow up), we would
    # get the lengths of the lists, then pad the shorter list with zeros in the front. 
    # Other logic would be the same, except for the carryover digit, which would need
    # to go to the previous node instead of the next node.
    # This would also have O(N) runtime.
    
    n_1 = ll_1
    n_2 = ll_2
    return_ll = Node(0)
    n_return = return_ll
    
    while not (n_1 is None and n_2 is None):  # O(N) loop, where N is the number of nodes in the larger list.
        
        # Sum the data.
        digit_sum = 0
        if n_1 is not None:
            digit_sum += n_1.data
            n_1 = n_1.next
        if n_2 is not None:
            digit_sum += n_2.data
            n_2 = n_2.next
        
        # Add the new node.
        if n_return.next is not None:
            digit_sum += n_return.next.data
        n_return.next = Node(digit_sum % 10)
        
        # If value is more than one digit, create next node.
        if digit_sum > 9:
            n_return.next.next = Node(digit_sum // 10)
            
        n_return = n_return.next
    
    return return_ll.next
    
    
# 2.6
# Check if a linked list is a palindrome.
# I'm assuming this is for a singly linked list, else it wouldn't be as hard.
#
# This method has O(N) runtime, where N=num_nodes.

def two_six(head):
    
    n_1 = head
    stack = []
    
    while n_1 is not None:  # O(N) loop.
        stack.append(n_1.data)
        n_1 = n_1.next
    
    n_2 = Node(stack.pop())  # O(1) operation.
    n_2_head = n_2
    while len(stack) != 0:  # O(N) loop.
        n_2.next = Node(stack.pop())  # O(1) operation.
        n_2 = n_2.next
    
    n_2.next = None
    n_1 = head
    n_2 = n_2_head
    while n_1 is not None:  # O(N) loop.
        print(n_1.data, n_2.data)
        if n_1.data != n_2.data:
            return False
        n_1 = n_1.next
        n_2 = n_2.next
    
    return True
    
    
    
a = llist_from_list([1,2,3,4,5,6,7,8,7,5,6,3,9])
print(two_six(a))


# 2.7
# Description
#
# This method has O(____) runtime, where N=____.

def two_seven():
    pass

# 2.8
# Description
#
# This method has O(____) runtime, where N=____.

def two_eight():
    pass
