# 15.Leet code
# 3sum

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Problem:
        --------
        Given an integer array `nums`, return all unique triplets [nums[i], nums[j], nums[k]]
        such that i != j, i != k, j != k, and nums[i] + nums[j] + nums[k] == 0.

        Notes:
        ------
        - The output must not contain duplicate triplets.
        - The order of triplets in the output doesn’t matter.

        Example:
        --------
        Input:  nums = [-1, 0, 1, 2, -1, -4]
        Output: [[-1, -1, 2], [-1, 0, 1]]

        Approach (Two-Pointer Technique):
        ---------------------------------
        1. Sort the array to easily skip duplicates and use two-pointer logic.
        2. Iterate through each element `nums[i]` as a potential first element.
        3. For each `i`, use two pointers:
           - `j` starts from i + 1 (next element)
           - `k` starts from the end of the list
        4. Compute current_sum = nums[i] + nums[j] + nums[k]
           - If current_sum == 0 → we found a triplet.
           - If current_sum < 0  → move left pointer (j += 1) to increase sum.
           - If current_sum > 0  → move right pointer (k -= 1) to decrease sum.
        5. Use a set to store triplets and automatically avoid duplicates.
        6. Convert the set to a list before returning.
        """

        target = 0  # We need triplets that sum up to 0
        nums.sort()  # Step 1: Sort the list to handle duplicates and apply two-pointer logic

        triplets = set()  # Using a set to store unique triplets

        # Step 2: Iterate through the list
        for i in range(len(nums)):
            # Step 3: Initialize two pointers
            j = i + 1
            k = len(nums) - 1

            # Step 4: While the two pointers don't cross each other
            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]  # Calculate the triplet sum

                # Case 1: Found a valid triplet
                if current_sum == target:
                    triplets.add((nums[i], nums[j], nums[k]))  # Store tuple in set (immutable)
                    j += 1  # Move left pointer forward
                    k -= 1  # Move right pointer backward

                # Case 2: Sum too small → increase it by moving left pointer
                elif current_sum < target:
                    j += 1

                # Case 3: Sum too large → decrease it by moving right pointer
                else:
                    k -= 1

        # Step 5: Convert the set of tuples to a list of lists for final output
        return list(triplets)

        # -------------------------------------------------------------
        # Time Complexity:  O(n^2)
        #   - Sorting: O(n log n)
        #   - Two-pointer search per element: O(n)
        #
        # Space Complexity: O(n)
        #   - Because of the set used to store unique triplets
        # -------------------------------------------------------------
