# Leetcode
# 380. Insert Delete GetRandom O(1)

import random

class RandomizedSet:
    def __init__(self):
        """
        Initialize two data structures:
        1. self.data_list -> stores all the elements for O(1) random access
        2. self.data_map -> stores element:value pairs (val -> index in list)
        """
        self.data_list = []     # list of current elements
        self.data_map = {}      # dictionary mapping element to its index in data_list

    def insert(self, val: int) -> bool:
        """
        Inserts an element into the set if not already present.
        Returns True if inserted successfully, False if already exists.
        Time Complexity: O(1)
        """
        if val in self.data_map:
            # If the value already exists, we cannot insert again
            return False
        
        # Add value to the end of list
        self.data_list.append(val)
        
        # Record the value's index in the map
        self.data_map[val] = len(self.data_list) - 1
        
        return True

    def remove(self, val: int) -> bool:
        """
        Removes an element from the set if present.
        Returns True if the element was removed, False if it didn't exist.
        Time Complexity: O(1)
        """
        if val not in self.data_map:
            # Value not found, cannot remove
            return False
        
        # Step 1: Find the index of element to remove
        idx_to_remove = self.data_map[val]
        
        # Step 2: Get the last element in the list
        last_element = self.data_list[-1]
        
        # Step 3: Move the last element into the position of the element being removed
        self.data_list[idx_to_remove] = last_element
        self.data_map[last_element] = idx_to_remove  # update its index in map
        
        # Step 4: Remove the last element (since it's now duplicated)
        self.data_list.pop()
        del self.data_map[val]  # delete the removed element from map
        
        return True

    def getRandom(self) -> int:
        """
        Returns a random element from the set.
        Each element has an equal probability of being returned.
        Time Complexity: O(1)
        """
        return random.choice(self.data_list)
