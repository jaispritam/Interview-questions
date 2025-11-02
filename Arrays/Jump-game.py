# Leet Code
# 55. Jump Game
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Determines if you can reach the last index of the array starting from the first index.

        Each element in 'nums' represents the maximum jump length you can take from that position.

        Approach:
        - Start from the end of the array (goal = last index).
        - Move backward and check if from index 'i' you can reach the current 'goal'.
        - If yes, update the goal to 'i' (meaning we can reach the end from here).
        - Finally, if the goal reaches 0, that means we can reach the last index starting from index 0.

        Example:
        nums = [2, 3, 1, 1, 4]
        -> Return True (we can reach the last index)

        nums = [3, 2, 1, 0, 4]
        -> Return False (we get stuck at index 3)

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        goal = len(nums) - 1  # Start with the last index as the goal

        # Move backwards through the array
        for i in range(len(nums) - 2, -1, -1):
            # If from index i, we can reach or go beyond the current goal
            if nums[i] + i >= goal:
                goal = i  # Move the goal to this position

        # If we can move the goal back to index 0, return True
        return goal == 0
