"""
Chapter Four - Trees and Graphs
"""

from collections import dequeue  # For BFS.


# Create graph class for use in problems.
class Graph:
    
    def __init__(self):
        pass
    
    def add_node(self, node):
        # Adds a node to the graph.
        pass

# Create a node class.
class Node:
    
    def __init__(self, value):
        self.value = value
        self.left = None  # For use in binary trees only.
        self.right = None  # For use in binary trees only.
        pass
    
    def get_adjacent(self):
        # Return list of all adjacent nodes.
        pass
    
    def add_adjacent(self, node):
        # Add node as adjacent to self.
        pass

# Creating a simple node class.
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


# 4.1
# Find if there is a path between two nodes S and E in a directed graph.
# 
# This method has worst-case O(N) runtime where N=num nodes in graph.

def four_one(graph, S, E):
    
    # We will do a BFS from S to find a path to E.
    if S == E:
        return True
    queue = dequeue()
    queue.append(S)
    visited = {S: True}
    
    while queue:  # O(N) loop worst-case.
        
        # Get current node from each.
        desc = queue.popleft()
        
        # Check all neighbors of queue.
        for node in desc.get_adjacent():
            if node == E:
                return True
            elif node in visited:
                continue
            else:
                queue.append()
                visited[node] = True
    
    return False


# 4.2
# Given a sorted array with unique integers, create a binary search tree with minimal height.
# I assume that making the tree balanced left/right will make it as short as possible.
# 
# This method has O(N) runtime where N=num integers in array.

def four_two(array):
    
    # Recursively add all data to the tree by index from array.
    def add_nodes(start, end):
        
        if end < start or start < 0 or end > (len(array)-1):
            return None
        
        middle = (end+start) // 2
        root = Node(array[middle])
        root.left = add_nodes(start, middle-1)
        root.right = add_nodes(middle+1, end)
        return root
    
    return add_nodes(0, len(array)-1)


# 4.3
# Create a linked list of all nodes for each layer of a binary tree.
# 
# This method has O(N) runtime where N=num nodes in tree.

def four_three(root):
    
    # Implement a DFS to get all items at each layer.
    ll_list = []
    ll_list.append([])  # Root layer.
    current_node = []  # Will hold current node for each layer.
    
    # Recursive function to get all nodes.
    def DFS(tree_node, layer):  # Should be called N times.
        
        # Make new linked list node for the current value.
        new_ll_node = LinkedListNode(tree_node.value)
        
        # Add a linked list for the current layer.
        if layer < len(ll_list)-1:
            ll_list.append(new_ll_node)
            current_node.append(new_ll_node)
        
        # Link the list, update current_node.
        else:
            current_node[layer].next = new_ll_node
            current_node[layer] = new_ll_node
        
        # Recurse for tree node children.
        DFS(tree_node.left, layer+1)
        DFS(tree_node.right, layer+1)
    
    DFS(root, 0)
    return ll_list


# 4.4
# Check if a binary tree is balanced.
# A balanced tree is defined as the two subtrees' heights not differing
# by more than one for any node in the tree.
# 
# This method has O(N) runtime where N=num nodes in tree.

def four_four(root):
    
    def layer_count(node, layer):
        
        if node == None:  # Came from a leaf node.
            return 0
        
        # Call function recursively for left and right nodes. If they return -1, pass the error up.
        sublayers_left = layer_count(node.left, layer+1)
        if sublayers_left == -1:
            return -1
        sublayers_right = layer_count(node.right, layer+1)
        if sublayers_right == -1:
            return -1
        
        # If num sublayers diff by more than 1, return -1.
        if abs(sublayers_left - sublayers_right) > 1:
            return -1
        else:
            return max(sublayers_left, sublayers_right)+1
    
    return layer_count(root, 0) != -1


# 4.5
# Check if a binary tree is a binary search tree.
# BST Definition: left node <= current node < right node, and
# that all left nodes must be less than all right nodes.
# 
# This method has O(N) runtime where N=num nodes in tree.


### INCOMPLETE
# I forgot the second BST requirement (above).

def four_five(root):
    
    def BST_check(node):
        
        if node.left is None and node.right is None:  # Leaf node; always valid BST.
            return True
        
        elif node.left is None:  # No left node.
            if node.right.value <= node.value:  # Not a BST.
                return False
            else:
                return BST_check(node.right)  # Check right node.
        
        elif node.right is None:  # No right node.
            if node.left.value > node.value:  # Not a BST.
                return False
            else:
                return BST_check(node.left)    # Check left node.
        
        else:  # Both nodes are valid.
            if node.left.value <= node.value and node.right.value > node.value:  # Valid BST.
                return min(BST_check(node.left), BST_check(node.right))
            else:
                return False
        
    return BST_check(root)


# 4.6
# Description
# 
# This method has O(____) runtime where N=____.

def four_six():
    pass


# 4.7
# Description
# 
# This method has O(____) runtime where N=____.

def four_seven():
    pass


# 4.8
# Description
# 
# This method has O(____) runtime where N=____.

def four_eight():
    pass


# 4.9
# Description
# 
# This method has O(____) runtime where N=____.

def four_nine():
    pass


# 4.10
# Description
# 
# This method has O(____) runtime where N=____.

def four_ten():
    pass


# 4.11
# Description
# 
# This method has O(____) runtime where N=____.

def four_eleven():
    pass


# 4.12
# Description
# 
# This method has O(____) runtime where N=____.

def four_twelve():
    pass
