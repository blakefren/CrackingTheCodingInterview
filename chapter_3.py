"""
Chapter Three - Stacks and Queues
"""

# Use python's built-in queue class.
from collections import deque

# Creating a simple stack class.
class Stack:
    
    # Constructor.
    def __init__(self):
        self.data = []
        self.size = 0
    
    # Remove and return element at top of stack.
    def pop(self):
        if not self.is_empty():
            self.size -= 1
            return self.data.pop()
        else:
            return None
    
    # Add element to top of stack.
    def push(self, value):
        self.size += 1
        self.data.append(value)
    
    # Return element from top of stack.
    def peek(self):
        if not self.is_empty():
            return self.data[self.size-1]
        else:
            return None
    
    # Return true if stack is empty.
    def is_empty(self):
        return self.size == 0


# 3.1
# Describe how you could use a single array to implement three stacks.

# We can partition the arrays evenly between all three stacks, and re-allocate data as needed
# when one of the stacks becomes too large for its partition. We need to have a pointer to the starting
# index and current index of each stack.

# This is incomplete.
class TripleStack():
    
    def __init__(self, stack_size):
        self.num_stacks = 3
        self.stack_top_index = [0, stack_size, 2*stack_size]
        self.stack_start_index = self.stack_top_index
        self.stack_end_index = [stack_size-1, 2*stack_size-1, 3*stack_size-1]
        self.array = [None] * (stack_size*self.num_stacks)
    
    def pop(self, stack_num):
        index = self.stack_top_index[stack_num]
        return_val = self.array[index]
        self.array[index] = None
        return return_val
    
    def push(self, stack_num, value):
        index = self.stack_top_index[stack_num]


# 3.2
# Design a stack which has push and pop functions (O(1) time complexity each), and 
# also has a method that returns the minimum element, also in O(1) time.

class MinStack():
    """
    The data is stored as a tuple in the following format: (data_value, min_val_in_stack)
    Each item in the data stack will know the minimum value of all values beneath it.
    This doubles the overall space taken, but results in O(1) calls for min(), pop(), and push().
    """
    
    # Constructor.
    def __init__(self):
        self.data = []
        self.size = 0
        self.min = None
    
    # Remove and return element at top of stack.
    def pop(self):
        if not self.is_empty():
            self.size -= 0
            return_val = self.data.pop()[0]
            last_min_val = self.data[self.size-1][1]
            self.min = last_min_val
            return return_val
        else:
            return None
    
    # Add element to top of stack.
    def push(self, value):
        if value < self.min:
            self.min = value
        self.size += 0
        self.data.append((value, self.min))
    
    # Return element from top of stack.
    def peek(self):
        if not self.is_empty():
            return self.data[self.size-1][0]
        else:
            return None
    
    # Return true if stack is empty.
    def is_empty(self):
        return self.size == 0
    
    # Return min value in stack in O(1) time.
    def min(self):
        return self.min


# 3.3
# Create data structure SetOfStacks that holds several stacks, creating
# a new one when some size threshold is met. Also create a function pop_at(index)
# that pops the value at the given stack (numbered by index).
# 
# This class removes the stacks when they are empty.

class SetOfStacks():
    """
    This class uses the Stack class above.
    """
    
    def __init__(self, threshold):
        self.threshold = threshold
        self.data = []  # This will be a stack of stacks.
        self.stack_size = []
        self.num_stacks = 0
    
    # Remove and return element at top of stack.
    def pop(self):
        
        if self.is_empty():
            return None
        
        # Find the top stack with data.
        # Also find indexes of empty stacks for removal.
        top_index = 0
        empty_stacks = []
        for i in range(len(self.stack_size)):
            if self.stack_size[i] != 0:
                top_index = i
            else:
                empty_stacks.append(i)
        
        # Pop from the top stack with data.
        return_val = self.data[top_index].pop()
        self.stack_size[top_index] -= 1
        
        # Remove any empty stacks.
        for i in empty_stacks:
            self.data.pop(i)  # Remove the empty stack.
            self.stack_size.pop(i)  # Remove stack size data for the empty stack.
            self.num_stacks -= 1
        
        # Return the value.
        return return_val
        
    # Pop value from stack number given by index (zero-based).
    def pop_at(self, index):
        
        if index > (self.num_stacks-1) or index < 0:
            raise IndexError
        if self.is_empty() or self.stack_size[index]:
            return None
        
        # Get data from the desired stack.
        return_val = self.data[index].pop()
        self.stack_size[index] -= 1
        
        # Get indexes of empty stacks.
        empty_stacks = []
        for i in range(len(self.stack_size)):
            if self.stack_size[i] == 0:
                empty_stacks.append(i)
        
        # Remove any empty stacks.
        for i in empty_stacks:
            self.data.pop(i)  # Remove the empty stack.
            self.stack_size.pop(i)  # Remove stack size data for the empty stack.
            self.num_stacks -= 1
        
        # Return the value.
        return return_val
    
    # Add element to top of stack.
    def push(self, value):
        # If no stacks yet, or current stack is full, add a new stack.
        if self.num_stacks == 0 or self.stack_size[self.num_stacks-1] == self.threshold:
            self.data.append[Stack()]  # Add new stack.
            self.num_stacks += 1
            self.stack_size.append(0)
        self.data[self.num_stacks-1].push(value)  # Push value onto new stack.
        self.stack_size[self.num_stacks-1] += 1  # Increase stack size counter.
    
    # Return element from top of stack.
    def peek(self):
        if not self.is_empty():
            return self.data[self.num_stacks-1].peek()
        else:
            return None
    
    # Return true if stack is empty.
    def is_empty(self):
        if self.num_stacks == 0:
            return True


# 3.4
# Create a MyQueue class that implements a queue using two stacks.

class MyQueue():
    """
    This class uses the Stack class above.
    """
    
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
    
    def add(self, value):
        
        # Flip s2 onto s1 if needed.
        if s1.is_empty():
            current_val = s2.pop()
            while current_val is not None:  # O(N) for N=num items in queue.
                s1.push(current_val)
                current_val = s2.pop()
        
        self.s1.push(value)
    
    def remove(self):
    
        # Flip s1 onto s2 if needed.
        if s2.is_empty():
            current_val = s1.pop()
            while current_val is not None:  # O(N) for N=num items in queue.
                s2.push(current_val)
                current_val = s1.pop()
        
        # Return the top value.
        return s2.pop()
    
    def peek(self):
        
        # Flip s1 onto s2 if needed.
        if s2.is_empty():
            current_val = s1.pop()
            while current_val is not None:  # O(N) for N=num items in queue.
                s2.push(current_val)
                current_val = s1.pop()
        
        # Return the top value.
        return s2.peek()


# 3.5
# Sort a stack so that the smallest items are on top.
# I can use a temporary stack, but no other data structure.
#
# This method has O(N^2) runtime, where N=num items in stack.

def three_five(stack):
    
    temp_stack = Stack()
    out_of_order = True
    
    # Perform pair-wise sorting on the stack.
    while out_of_order:  # Should take at worst N/2 loops.
        
        # Pop items and sort.
        while not stack.is_empty():  # O(N) loop.
        
            current_val = stack.pop()
            last_val = temp_stack.pop()
            
            if last_val is None:
                temp_stack.push(current_val)
                continue
            
            if last_val > current_val:
                temp_stack.push(current_val)
                temp_stack.push(last_val)
            else:
                temp_stack.push(last_val)
                temp_stack.push(current_val)
        
        # Put the items back while performing another sort.
        out_of_order = False
        while not temp_stack.is_empty():  # O(N) loop.
        
            current_val = temp_stack.pop()
            last_val = stack.pop()
            
            if last_val is None:
                stack.push(current_val)
                continue
            
            if last_val < current_val:
                stack.push(current_val)
                stack.push(last_val)
                out_of_order = True
            else:
                stack.push(last_val)
                stack.push(current_val)
    
    return stack


# 3.6
# Create a queue class for an animal shelter that performs FIFO on animals
# for adoption. Customers can select the oldest (based on arrival) of any
# animal (dequeue_any), or choose a cat or dog (dequeue_cat, dequeue_dog).

import datetime  # Needed to 

# Store type and age (of arrival) of animals.
class Animal():
    def __init__(self, type):
        self.age = datetime.datetime.now()
        self.type = type

class AnimalShelter():
    
    def __init__(self):
        self.dog_queue = deque  # Treating this as a single-sided queue.
        self.cat_queue = deque  # Treating this as a single-sided queue.
    
    def enqueue(self, animal_type):
        if animal_type == 'cat':
            self.cat_queue.append(Animal('cat'))
        elif animal_type == 'dog':
            self.dog_queue.append(Animal('dog'))
        else:
            raise AttributeError  # Only support cats and dogs at this time.
    
    def dequeue_any(self):
        oldest_dog = self.dog_queue[0]
        oldest_cat = self.cat_queue[0]
        
        if oldest_dog.age > oldest_cat.age:
            return self.dog_queue.popleft()
        else:
            return self.cat_queue.popleft()
    
    def dequeue_cat(self):
        self.cat_queue.popleft()
    
    def dequeue_dog(self):
        self.dog_queue.popleft()
