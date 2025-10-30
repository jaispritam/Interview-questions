# 169. Leet code
# Majority Element

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # -------------------------------------------------------------
        # Problem:
        # Given an array nums of size n, return the majority element.
        # The majority element is the one that appears more than ⌊n / 2⌋ times.
        # It is guaranteed that such an element always exists.
        #
        # Example:
        # Input: nums = [2,2,1,1,1,2,2]
        # Output: 2
        # -------------------------------------------------------------

        # Step 1: Find the length of the list
        n = len(nums)

        # Step 2: Calculate half of that length (using floor division)
        # Because the majority element must appear more than n/2 times
        half = n // 2

        # Step 3: Convert the list to a set to get unique elements
        # This avoids counting the same number multiple times unnecessarily
        unique_nums = set(nums)

        # Step 4: Loop through each unique number
        for num in unique_nums:
            # Count how many times the current number appears in the original list
            count = nums.count(num)

            # Step 5: Check if this number appears more than n/2 times
            if count > half:
                # If yes, then it's the majority element — return it immediately
                return num

        # Note: No need for a default return because the problem guarantees
        # that a majority element always exists.

        # -------------------------------------------------------------
        # Time Complexity:  O(n^2)
        # - Because nums.count(num) is O(n) and we may call it up to n times
        #
        # Space Complexity: O(n)
        # - Because of the use of a set to store unique elements
        #
        # This is simple and readable but not the most efficient method.
        # -------------------------------------------------------------
