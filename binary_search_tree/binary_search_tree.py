"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
            # Case 1: value is less than self.value
        if value < self.value:

            # If there is no left child, insert value here
            if self.left is None:
                self.left = BSTNode(value)

            # Else ??????
            else:
                # repeat the process on the left subtree
                self.left.insert(value)


        # Case 2: value is greater or equal to than self.value
        elif value >= self.value:

            if self.right is None:
                self.right = BSTNode(value)

            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # forget about the left subtree
        # iterate through the nodes using a loop most likely the while loop
        current = self
        next_node = current.right

        while next_node is not None:
            current = next_node
            next_node = self.right.right
        
        return current.value
        # maximum = 0
        # current = self
        # while current is not None:
        #     if current.value > maximum:
        #         maximum = current.value
        #     current = current.right
        # return maximum

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # we need a function to handle the right using a loop
        # we need an identical function to handle it for the left
        # we need these functions to be called recursively
        fn(self)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
