from random import randint

def quick_sort(array, min_index=0, max_index=-1):
    
    if max_index == -1:
        max_index = len(array) - 1
    if (min_index >= max_index):
        return array
    
    # Pick a random element to be the first pivot and swap to the end.
    pivot_index = randint(min_index, max_index)
    pivot = array[pivot_index]
    temp = array[max_index]
    array[max_index] = pivot
    array[pivot_index] = temp
    
    # Set swap_index so that we ignore elements at left
    # that are less than the pivot.
    swap_index = 0
    while array[swap_index] < pivot:
        swap_index += 1
    
    # Put all elements less than pivot to the left of pivot.
    for i in range(min_index, max_index + 1):  # O(N).
        
        # If element is smaller than pivot and is to the right of other
        # elements less tan pivot, swap it.
        if array[i] < pivot and i > swap_index:
            temp = array[swap_index]
            array[swap_index] = array[i]
            array[i] = temp
            while array[swap_index] < pivot:
                swap_index += 1
    
    # Swap the pivot into its sorted position.
    array[max_index] = array[swap_index]
    array[swap_index] = pivot
    
    # Recursive call if needed.
    if swap_index > min_index:
        array = quick_sort(array, min_index, swap_index-1)
    if swap_index < max_index:
        array = quick_sort(array, swap_index+1, max_index)
    
    return array
