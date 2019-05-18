"""
Chapter Fifteen - Moderate
"""

from time import sleep
from datetime import datetime
from threading import Lock, Thread, Semaphore
from multiprocessing import Pool

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

    def _mark_nodes_unvisited(self):
        for function in self.functions:  # Mark all as unvisited.
            self.functions[function] = False

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
                    self._mark_nodes_unvisited()
                    return False  # Graph is cyclic.

                if not self.functions[func]:  # If not visited, add to the queue.
                    queue.append(func)

                self.functions[func] = True  # Mark as visited.

        self._cyclic = False
        self._new_nodes = False
        self._mark_nodes_unvisited()

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
# Given class Foo below and three threads, where one of each will execute first, one second, and one third,
# design a mechanism to ensure that methods first, second, are called in order and completed before the
# next thread is called.

class Foo:

    def __init__(self):
        self.sem = Semaphore(1)  # One thread at a time.

    def first(self):
        self.sem.acquire()
        print('\nfirst start - ' + str(datetime.now()))
        sleep(1)
        print('first end - ' + str(datetime.now()))
        self.sem.release()

    def second(self):
        self.sem.acquire()
        print('\nsecond start - ' + str(datetime.now()))
        sleep(1)
        print('second end - ' + str(datetime.now()))
        self.sem.release()

    def third(self):
        self.sem.acquire()
        print('\nthird start - ' + str(datetime.now()))
        sleep(1)
        print('third end - ' + str(datetime.now()))
        self.sem.release()

def fifteen_five():
    
    foo = Foo()

    # Create three threads.
    targets = [Thread(target=foo.first()), Thread(target=foo.second()), Thread(target=foo.third())]
    threads = []

    # Execute them in order.
    for i in range(3):
        t = targets[i]
        threads.append(t)
        t.start()


# 15.6
# Given a class with a synchronized method A and a normal method B and two threads, (1) can both threads
# execute A at the same time, and (2) can one execute A and one execute B.

def fifteen_six():

    """
    For my sanity: a synchronized method in a class means that it can only be run by one thread
    at a time for a single object instance.

    (1) - no, assuming we're talking about a single instance of the object
    (2) - yes
    """

    pass


# 15.7
# Implement FizzBuzz with four threads. (1) checks for divisibility by 3 and prints "Fizz", (2) checks for
# divisibility by 5 and prints "Buzz", (3) checks for divisibility by 3 and 5 and prints "FizzBuzz", and (4)
# handles the remaining numbers.
#
# My method doesn't print them in order, but it prints them.

def t_one(n):
    for num in range(1, n + 1):
        if num % 3 == 0 and num % 5 == 0:
            print(str(num) + ' - FizzBuzz')

def t_two(n):
    for num in range(1, n + 1):
        if num % 3 == 0 and num % 5 != 0:
            print(str(num) + ' - Fizz')

def t_three(n):
    for num in range(1, n + 1):
        if num % 3 != 0 and num % 5 == 0:
            print(str(num) + ' - Buzz')

def t_four(n):
    for num in range(1, n + 1):
        if num % 3 != 0 and num % 5 != 0:
            print(str(num))


def fifteen_seven(n):

    threads = []
    targets = [Thread(target=t_one(n)), Thread(target=t_two(n)), Thread(target=t_three(n)), Thread(target=t_four(n))]

    for i in range(4):
        t = targets[i]
        threads.append(t)
        t.start()
