from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Problem:
        ----------
        Given an integer array nums, return an array 'output' such that:
            output[i] = product of all elements of nums except nums[i].

        Constraints:
        - You must solve it in O(n) time.
        - You cannot use the division operation.
        - The product of any prefix or suffix fits in a 32-bit integer.

        Approach:
        ----------
        The trick is to compute the product of elements to the left and right
        of each index *without* using division.

        1️⃣ Step 1: Forward Pass
            - Traverse from left to right.
            - For each index i, store the product of all numbers to its left.
            - Keep updating a running 'left' product as you go.

        2️⃣ Step 2: Backward Pass
            - Traverse from right to left.
            - For each index i, multiply the current value in output[i]
              (which already contains the left product)
              by the 'right' product (product of all numbers to the right).
            - Keep updating a running 'right' product.

        This ensures that each index gets:
            output[i] = (product of elements to the left of i) * (product of elements to the right of i)

        Time Complexity:  O(n)
        Space Complexity: O(1) extra (output array doesn't count as extra space)
        """

        # Initialize the output array with 1s
        output = [1] * len(nums)
        
        # ---------- Forward Pass ----------
        # Calculate prefix (left) products
        left = 1
        for i in range(len(nums)):
            output[i] *= left       # Assign the product of all elements to the left of index i
            left *= nums[i]         # Update left product for the next index
        
        # ---------- Backward Pass ----------
        # Calculate suffix (right) products
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= right      # Multiply with product of all elements to the right of index i
            right *= nums[i]        # Update right product for the next index on the left

        return output
