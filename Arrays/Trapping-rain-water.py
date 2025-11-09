# Leetcode
# 42. Trapping Rain Water

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Calculate the total amount of rainwater that can be trapped between the bars.

        Parameters:
        height (List[int]): A list of non-negative integers representing the elevation map,
                            where the width of each bar is 1.

        Returns:
        int: Total units of trapped rainwater.
        """

        # Initialize two pointers at the start and end of the array
        left = 0
        right = len(height) - 1

        # Initialize the maximum height seen so far from the left and right
        left_max = height[left]
        right_max = height[right]

        # Variable to store the total trapped water
        water = 0

        # Traverse the array until the two pointers meet
        while left < right:
            # Compare left_max and right_max to decide which side to move
            if left_max < right_max:
                # Move the left pointer to the right
                left += 1
                # Update left_max if the new bar is higher
                left_max = max(left_max, height[left])
                # Water trapped at current bar = left_max - height[left]
                water += left_max - height[left]
            else:
                # Move the right pointer to the left
                right -= 1
                # Update right_max if the new bar is higher
                right_max = max(right_max, height[right])
                # Water trapped at current bar = right_max - height[right]
                water += right_max - height[right]
        
        # Return the total trapped water
        return water
