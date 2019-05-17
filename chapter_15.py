"""
Chapter Fifteen - Moderate
"""

from threading import Lock

# 15.1
# Description
# 
# This method has O(____) runtime, where ____=____.

def fifteen_one():
    
    pass


# 15.2
# Description
# 
# This method has O(____) runtime, where ____=____.

def fifteen_two():
    
    pass


# 15.3
# Imagine a table of philosophers trying to eat with chopsticks. They each need both chopsticks to eat, but
# there is only one chopstick between each philosopher. They always reach for the left one first.
# Write a simulation of this using threads and locks that avoids a deadlock.

def fifteen_three():

    """
    The book's solutions:

    1 - have the philosopher put down a chopstick if he is unable to get the second one
    2 - give the chopsticks a priority so that the guy at the "end" of the circular table
        picks up the right one first (doesn't this break the rules in the prompt?).

    Problems with 1: if all philosopher instances are perfectly synchronized, they will all pick up
    the left chopstick, not be able to get the right one, and then put down the left one and start over.
    This could lead to its own lock, though it isn't a deadlock - it's a livelock.

    Problems with 2: if we assume that the philosophers always have to pick up the left stick first,
    then this breaks the rules of the prompt. Of course, in the real world, this doesn't matter so much.
    Requirements can be modified if needed, or if they are not feasible.

    Other solutions ("inspired" by Wikipedia):
    3 - use an "arbitrator" who tells each philosopher when they can pick up both sticks and begin eating.
        The arbitrator will need to have visibility to all chopsticks and the state of each
        philosopher, however.
    """

    pass


# 15.4
# Design a class which provides a lock only if there are no possible deadlocks.

class fifteen_four:

    # We will store the functions and their dependencies as a directed graph.
    # If the graph has a cycle, then there will be a deadlock.

    def __init__(self):
        self.functions = {}
        self.function_dependencies = {}
        self.locked = False
        self._cyclic = False
        self._new_nodes = True

    def register_function(self, function_name, dependencies_lst):
        self._new_nodes = True
        self.functions[function_name] = False  # To mark as visited during graph search.
        # dependencies_lst is assumed to be a list of function_names.
        self.function_dependencies[function_name] = dependencies_lst

    def get_lock(self, function_name):

        # Need to check for a cycle in our graph.
        # All functions must be registered before checking for a lock for accuracy.
        # We'll just do a BFS for simplicity.
        # Returns True if lock is set, False otherwise.

        if self._cyclic and not self._new_nodes:
            return False

        # register_function has not been run for this function.
        if function_name not in self.functions or function_name not in self.function_dependencies:
            return False

        queue = deque()
        queue.append(function_name)
        while queue:

            for func in self.function_dependencies[queue.popleft()]:

                if func == function_name:
                    self._cyclic = True
                    self._new_nodes = False
                    return False  # Graph is cyclic.

                if not self.functions[func]:  # If not visited, add to the queue.
                    queue.append(func)

                self.functions[func] = True  # Mark as visited.

        self._cyclic = False
        self._new_nodes = False
        for function in self.functions:  # Mark all as unvisited.
            self.functions[function] = False

        self.locked = Lock.acquire(True, timeout=10)  # Give it 10 seconds to get a lock.
        return self.locked

    def release_lock(self):

        if self.locked:
            Lock.release()
            self.locked = False
            return True

        else:
            return False


# 15.5
# Description
# 
# This method has O(____) runtime, where ____=____.

def fifteen_five():
    
    pass


# 15.6
# Description
# 
# This method has O(____) runtime, where ____=____.

def fifteen_six():
    
    pass


# 15.7
# Description
# 
# This method has O(____) runtime, where ____=____.

def fifteen_seven():
    
    pass
