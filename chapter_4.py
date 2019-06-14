"""
Chapter Four - Trees and Graphs
"""

from collections import deque  # For BFS.


# Pseudo graph class.
class Graph:
    
    def __init__(self):
        self.nodes = {}
        self.edges = {}  # Dict of lists for each node.
        self.reverse_edges = {}  # Dict of lists for each node.
        pass
    
    def add_node(self, node):
        # Adds a node to the graph in self.nodes.
        pass
    
    def add_edge(self, node_1, node_2):
        # Adds an edge to the graph from node_1 to node_2 in self.edges.
        # If node_1 or node_2 do not exist, create them and add to self.nodes.
        # Updates each node's adjacent and reverse_adjacent dicts as needed.
        pass
    
    def remove_node(self, node):
        # Removes a node, its edges, and its reverse edges.
        if node in self.nodes:
            del self.nodes[node]
        self.remove_nodes(node)
    
    def remove_edge(self, node_1, node_2):
        # Removes the edge and the reverse edge between node_1 and node_2.
        pass
    
    def remove_edges(self, node):  # O(1) with dicts.
        # Removes all edges and reverse edges for a single node.
        if node in self.edges:
            del self.edges[node]
        if node in self.reverse_edges:
            del self.reverse_edges[node]

# Pseudo node class.
class Node:
    
    def __init__(self, value):
        self.value = value
        self.left = None  # For use in binary trees only.
        self.right = None  # For use in binary trees only.
        self.adjacent = {}  # All downstream directed adjacent nodes.
        self.reverse_adjacent = {}  # All upstream directed adjacent nodes.
    
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
    queue = deque()
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
# all left nodes must be less than all right nodes.
# 
# This method has worst-case O(N) runtime where N=num nodes in tree.

import sys

def four_five(root):
    
    def BST_check(node, min, max):
        
        if node.left is None and node.right is None:  # Leaf node; always valid BST.
            return True
        
        elif node.left is None:  # No left node.
            if node.value < node.right.value <= max:   # Check right node.
                return BST_check(node.right, node.value, max)
            else:  # Not a BST.
                return False
        
        elif node.right is None:  # No right node.
            if min <= node.left.value <= node.value:   # Check left node.
                return BST_check(node.left, min, node.value) 
            else:  # Not a BST.
                return False
        
        else:  # Both nodes are valid.
            if (min <= node.left.value <= node.value) and (node.value < node.right.value <= max):  # Valid BST.
                return min(BST_check(node.left, min, node.value), BST_check(node.right, node.value, max))
            else:  # Not a BST.
                return False
    
    return BST_check(root, -sys.maxsize, sys.maxsize)  # Set initial bounds as max and min system value.


# 4.6
# Find the next node (in-order successor) of a given node in a binary search tree.
# Assume that each node has a link to its parent (let's say it's node.parent).
# In-order: left, current, right.
# 
# This method has O(N) runtime where N=num nodes in tree.

def four_six(node):
    
    if node = None:
        return None
    
    # Return the leftmost node in the right tree if the right node exists.
    if node.right:
        n_c = node.right
        while n_c.left:
            n_c = n_c.left
        return n_c
    
    # Since our node is the right node of the parent, then we need to go up
    # the chain until a parent is the left node of its parent.
    n_p = parent
    current = node
    while n_p and current != n_p.left:
        current = n_p
        n_p = n_p.parent
    return n_p


# 4.7
# Given a list of projects and dependencies (other projects), find the order the
# projects must be built in. All of a project's dependencies must be built before
# the project. The dependency list is a list of project pairs, where the second
# project is dependent on the first.
# Return an error if there is no valid build order.
# 
# This method has O(M+N^2) runtime where N=num projects and M=num dependencies.
# The book solution's runtime is incorrect; it should be the same as mine.

def four_seven(projects, dependencies):
    
    # Assume projects is a list, and dependencies is a list of tuples.
    # Build a graph of all projects (nodes) and dependencies (edges).
    
    g = Graph()
    queue = deque()
    
    for p in projects:  # O(N) loop.
        g.add_node(p)
        queue.append(p)
    
    for d in dependencies:  # O(M) loop.
        g.add_edge(d[0], d[1])
    
    order = []
    
    # Get all nodes that have no dependencies.
    # If no dependencies, add to order list and remove edges from graph.
    # Repeat until we've found all the nodes.
    loop_count = 0
    while queue:  # O(N) loop.
    
        n = queue.popleft()
        
        if n not in g.reverse_edges:
        
            order.append(n.value)
            g.remove_edges(n)  # O(1) removal.
            loop_count = 0
        
        else:
        
            queue.append(n)
            loop_count += 1
            
            # If we've found this many nodes with dependencies
            # in a row, then we have a circular loop in our graph.
            if loop_count >= len(projects):
                return None
    
    return order


# 4.8
# Find the first common ancestor of two nodes in a binary tree (not a BST).
# Do not store additional nodes in a data structure.
# 
# This method has O(N) runtime where N=depth of the deeper node.

def four_eight(a, b):
    
    # Get depths of a and b nodes, and find the deeper node.
    d_a = get_depth(a)
    d_b = get_depth(b)
    depth_diff = d_a - d_b
    deep = a if depth_diff > 0 else b
    shallow = b if depth_diff > 0 else a
    
    # Bring the deeper node to the height of the other.
    while depth_diff != 0:
        deep = deep.parent
        depth_diff -= 1
    
    while deep != shallow and deep and shallow:
        deep = deep.parent
        shallow = shallow.parent
    
    if deep and shallow:
        return deep
    else:
        return None
    
    def get_depth(node):
        depth = 0
        while node:
            node = node.parent
            depth += 1
        return depth


# 4.9
# Given a BST with distinct elements, return all possible arrays that could have
# been used to build the tree. The arrays were used to build the tree by
# inserting values from left to right.
#  
# This method has O(N^3+) runtime where N=num nodes in tree.

def four_nine(root):
    
    # Using a recursive solution (with DFS).
    # Need each subtree to return a list of lists of the arrays that could have built it.
    # Need to combine the list of lists from the left and right subtree for each node while maintaining order for each of the respective array options.
    # For each node, the first array item (prefix) is always that node.
    # I'm using a deque because it gives O(1) for pop/append for front and back.
    
    def get_array(node):  # Should run N times (that actually do something).
        
        if node is None:
            return deque([])  # Return an empty queue in a list to force one loop for permutations.
        
        # Get all options from left and right nodes, then make permutations and return.
        return_queue = deque()  # Will be a queue of queues.
        q_1 = get_array(node.left)
        q_2 = get_array(node.right)
        
        while q_1:  # O(N) loop.
        
            q_1_sub = q_1.popleft()
            while q_2:  # O(N) loop.
                
                q_2_sub = q_2.popleft()
                return_queue.extend(get_ordered_permutations(deque(node.value), q_1_sub, q_2_sub))
        
        return return_queue
        
        
    def get_ordered_permutations(prefix, q_1, q_2):  # Return a queue of queues of ordered permutations.
        
        return_queue = deque()
        
        if len(q_1) == 0:
            return_queue.extend([prefix + q for q in q_2])
            
        elif len(q_2) == 0:
            return_queue.extend([prefix + q for q in q_1])
        
        else:
            # Starting with left node.
            prefix.append(q_1.popleft())
            return_queue.extend(get_ordered_permutations(prefix, q_1, q_2))
            q_1.appendleft(prefix.pop())
            
            # Starting with right node.
            prefix.append(q_2.pop())
            return_queue.extend(get_ordered_permutations(prefix, lst_1, q_2))
            q_2.appendleft(prefix.pop())
        
        return return_queue
    
    return get_array(root)


# 4.10
# T1 and T2 are very large binary trees (not BSTs). T1 >> T2.
# Find if T2 is a subtree of T1.
# 
# This method has O(NxM) worst-case runtime where N=num nodes in T1 and M=num nodes in T2.
# Average case runtime is probably closer to O(N+kM), where k is the number of nodes in T1 that are the same as T2.

def four_ten(T1, T2):
    
    # Because T1 is very large, I assume it would be best to perform a pre-ordered
    # DFS to look for the head of T2 (n), then check all subnodes of n.
    # A BFS would require storing a large number of nodes in a queue while searching.
    # However, the DFS will require a large number of recursive threads. If the depth
    # of the tree is greater than the allowed recursion depth (~999 by default in Python),
    # the algorithm will fail.
    
    
    def DFS(node, T2_root):
        
        # Check current node against T2_root; if equal, check children in order.
        
        if node == None:
            return False
        
        if node == T2_root and subnode_DFS(node, T2_root):
            return True
        
        return DFS(node.left, T2_root) or DFS(node.right, T2_root)
    
    
    def subnode_DFS(node_1, node_2):
        
        # Check subtrees of node_1 and node_2 to see if they are identical.
        if node_1 == node_2:
            if node_1 is None and node_2 is None:
                return True
            else:
                return subnode_DFS(node_1.left, node_2.left) and subnode_DFS(node_1.right, node_2.right)
        
        return False
    
    
    if T2 is None:  # Null node is a subtree.
        return True
    
    return DFS(T1, T2)


# 4.11
# Implement a BST class with method getRandomNode that returns a random node in the tree.
# Each node should have an identical chance of being chosen.
# 
# This method has O(____) runtime where N=____.

from random import uniform

class four_eleven():
    """
    Class for a binary search tree, using the Node class above.
    It assumes node.left <= node < node.right.
    """
    
    def __init__(self):
        self.head = None
        self.num_nodes = 0
    
    def insert(self, data):
        # Returns success/failure as boolean.
        
        if self.head is None:
            
            self.head = Node(data)
            return True
        
        else:
            
            def insert_iterate(node):
                
                if node is None:
                    return False
                    
                elif data <= node.value:
                    if node.left is None:
                        node.left = Node(data)
                        return True
                    else:
                        return insert_iterate(node.left)
                        
                elif node.value < data
                    if node.right is None:
                        node.right = Node(data)
                        return True
                    else:
                        return insert_iterate(node.right)
                        
            return_val = insert_iterate(self.head)
            if return_val:
                self.num_nodes += 1
            return return_val
    
    def find(self, data):
        # Uses DFS.
        # If there are duplicate nodes, returns the first one found (highest in tree).
        
        def DFS(node):  # In-order depth-first search.
            if node and node.value == data:
                return node
            elif data <= node.value:
                return DFS(node.left)
            elif node.value < data:
                return DFS(node.right)
            return None
        
        n = self.head
        return DFS(n)
    
    def delete(self, data):
        # Uses DFS.
        
        node = self.find(data)
        if node:
            if node.left or node.right:  # Children nodes.
                # TODO: reinsert the values below this node.
                pass # return False
            else:  # No children nodes.
                del node
                self.num_nodes -= 1
                return True
        else:
            return False
    
    def getRandomNode(self):
        # Go through all nodes in tree until one matches a
        # predetermined random number or we run out of nodes.
        # This has O(N) runtime at worst, for N=num_nodes.
        
        def iterate(node, rand_num, node_count):
            node_count += 1
            if node is None:
                return None
            elif rand_num = node_count or node_count == self.num_nodes:
                return node
            else:
                n = iterate(node.left, rand_num, node_count)
                if n:
                    return n
                else:
                    return iterate(node.right, rand_num, node_count)
            
        return iterate(self.head, int(uniform(1, self.num_nodes)), 0)


# 4.12
# Given a binary tree (not BST), count the number of downward paths that equal a sum.
# The path can start at any node, and end at any node.
# 
# This method has O(N * log N) runtime where N=num nodes in tree, and O(1) space.
# An improvement can be made to change this to O(N) time and O(log N) space, but I'm tired.

def four_twelve(tree, sum):
    
    # This calls trigger_iterate for each node in the tree.
    # trigger_iterate calls sum_iterate, which sums all paths from a
    # specific node in the tree. Both methods return path_count, which
    # is the running sum of paths that meet the sum criteria.
    
    def sum_iterate(tree_node, running_sum, path_count):  # Runs once for each node, for each node above it.
        
        if tree_node is None or running_sum > sum:
            return path_count
        elif running_sum == sum:
            return path_count + 1
        
        if tree_node.left:
            path_count += sum_iterate(tree_node.left, running_sum+tree_node.value, path_count)
        if tree_node.right:
            path_count += sum_iterate(tree_node.right, running_sum+tree_node.value, path_count)
        
        return path_count
    
    def trigger_iterate(node, path_count):  # Runs N times.
        
        if node is None:
            return path_count
        
        path_count += sum_iterate(node.left, node.value, path_count)
        trigger_iterate(node.left, path_count)
        
        path_count += sum_iterate(node.right, node.value, path_count)
        trigger_iterate(node.right, path_count)
        
        return path_count
    
    return trigger_iterate(tree, 0)
