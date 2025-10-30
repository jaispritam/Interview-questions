#189 Leet code
# Rotate Array

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotates the array to the right by k steps (in-place).
        Example:
        --------
        Input:  nums = [1,2,3,4,5,6,7], k = 3
        Output: [5,6,7,1,2,3,4]

        Steps:
        - Rotate 1 step → [7,1,2,3,4,5,6]
        - Rotate 2 steps → [6,7,1,2,3,4,5]
        - Rotate 3 steps → [5,6,7,1,2,3,4]
        """

        # -------------------------------------------------------------
        # Step 1: Find the length of the list
        n = len(nums)

        # Step 2: Handle cases where k >= n
        # Rotating by n or a multiple of n gives the same array.
        # So we take k modulo n to get the effective rotation.
        k %= n

        # Step 3: Reverse the entire array
        # After this, the array becomes reversed:
        # Example: [1,2,3,4,5,6,7] → [7,6,5,4,3,2,1]
        nums.reverse()

        # Step 4: Reverse the first 'k' elements
        # This moves the last 'k' numbers (which should go to the front)
        # back into their correct relative order.
        # Example (k=3): reverse first 3 → [5,6,7,4,3,2,1]
        nums[:k] = reversed(nums[:k])

        # Step 5: Reverse the remaining 'n-k' elements
        # This restores the order of the rest of the elements.
        # Example: reverse from index 3 onward → [5,6,7,1,2,3,4]
        nums[k:] = reversed(nums[k:])

        # -------------------------------------------------------------
        # After all reversals, the array is rotated in-place.
        # No extra space is used, and the time complexity is linear.
        # -------------------------------------------------------------

        # Time Complexity:  O(n)
        # Space Complexity: O(1)
        # -------------------------------------------------------------
