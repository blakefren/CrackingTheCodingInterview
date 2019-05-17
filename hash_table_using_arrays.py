# Implement a hash table using only arrays.
# This hash table only takes integers, however, it can be modified to use any type.

from copy import deepcopy

class hash_table:
    
    def __init__(self):
        self._size = 0
        self._max_size = 1
        self._array = [None]
        
        # We could just calculate all primes at resize time instead of storing them.
        self._primes = [2, 3]  # Pretend this is an array too.
    
    
    def _calculate_hash(self, value):
        
        # Can modify this method to change the input data type.
        
        return value % self._max_size
    
    
    def get_size(self):
        return self._size
    
    
    def get_value(self, value):
        hash_index = self._calculate_hash(value)
        return self._array[hash_index]
    
    
    def insert_value(self, value):
        
        # Collision handling.
        hash_index = self._calculate_hash(value)
        if self._array[hash_index] is not None:
            self._expand_table()
            hash_index = self._calculate_hash(value)
        
        # Actually insert the value.
        self._array[hash_index] = value
        self._size += 1
    
    
    def _is_prime(self, value):
        
        for prime in self._primes:
            if value % prime == 0:
                return False  # Not prime.
            elif prime ** 2 >= value:
                return True  # Prime.
        
        # Need to calculate and save more primes.
        num = self._primes[len(self._primes) - 1] + 2
        while num ** 2 <= value:
            
            not_prime = False  # False = prime.
            for prime in self._primes:
                if num % prime == 0:
                    not_prime = True
                    break
                elif prime ** 2 >= num:  # Went up to the square root.
                    break  # Prime.
            
            if not not_prime:  # It's a prime.
                self._primes.append(num)
                if value % num == 0:
                    return False
                
            num += 2
        
        return True
    
    
    def _expand_table(self):
        
        # Double the table size and round up to the nearest
        # prime number, then fill new elements with None values.
        self._max_size = 2 * self._max_size + 1  # Always make it odd.
        
        while not self._is_prime(self._max_size):
            self._max_size += 2
        
        temp_array = deepcopy(self._array)
        self._array += [None] * (self._max_size - len(temp_array))  # Pretend I'm using real arrays.
        
        for value in temp_array:
            
            # Check that we aren't inserting a None value.
            if value is None:
                continue
            
            # Get new hash index.
            hash_index = self._calculate_hash(value)
            
            # Insert the old data.
            self._array[hash_index] = value
