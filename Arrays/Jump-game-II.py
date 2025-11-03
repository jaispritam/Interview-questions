# ================================================================
#  Problem: Jump Game II (Leetcode #45)
#  Difficulty: Medium
#  Topic: Greedy Algorithm
#  Author: Pritam Jais
#  Description:
#     You are given an integer array 'nums' where each element represents
#     the maximum number of steps you can move forward from that position.
#     You start at index 0 and must reach the last index (n - 1)
#     in the minimum number of jumps possible.
#
#     It is guaranteed that you can always reach the end.
# ================================================================

# -------------------------
# Example 1:
# Input:  nums = [2, 3, 1, 1, 4]
# Output: 2
# Explanation:
#   - Jump 1 step from index 0 → 1
#   - Jump 3 steps from index 1 → 4
#
# Example 2:
# Input:  nums = [2, 3, 0, 1, 4]
# Output: 2
# Explanation:
#   - Jump 1 step from index 0 → 1
#   - Jump 3 steps from index 1 → 4
# -------------------------


class Solution:
    def jump(self, nums):
        """
        ------------------------------------------------------------
        Function: jump
        Purpose:
            Calculates the minimum number of jumps required to reach
            the last index in the array 'nums'.
        ------------------------------------------------------------

        Parameters:
            nums (List[int]): A list of integers where each element
                              represents the maximum jump length
                              possible from that index.

        Returns:
            int: The minimum number of jumps needed to reach the last index.

        ------------------------------------------------------------
        Algorithm (Greedy Approach):
            1. We traverse through the array and keep track of:
                - 'farthest': The farthest index we can reach so far.
                - 'currentEnd': The end of the current jump’s range.
                - 'jumps': Total number of jumps made so far.

            2. For each index 'i', we update 'farthest' to the maximum
               reachable index using nums[i].

            3. When we reach 'currentEnd', it means we have to make
               another jump to extend our range up to 'farthest'.

            4. This continues until we reach or pass the last index.

            5. This approach ensures we always take the minimum jumps
               because we extend the range optimally before jumping.
        ------------------------------------------------------------
        """

        # Initialize variables
        jumps = 0          # Count of total jumps taken
        currentEnd = 0     # The end of the range for the current jump
        farthest = 0       # The farthest index we can reach currently

        # We stop at len(nums) - 1 because once we reach the last index,
        # we don't need to jump again
        for i in range(len(nums) - 1):

            # Update the farthest reachable index from current index 'i'
            farthest = max(farthest, i + nums[i])

            # If we reach the end of our current jump range
            # we need to make another jump
            if i == currentEnd:
                jumps += 1            # We take a jump
                currentEnd = farthest # Extend range to farthest we can reach

        # After loop ends, 'jumps' holds the minimum number of jumps
        return jumps


# -------------------------
# ✅ Example Test Run
# -------------------------
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums1 = [2, 3, 1, 1, 4]
    print("Input:", nums1)
    print("Minimum jumps required:", solution.jump(nums1))
    # Expected Output: 2

    print()

    # Example 2
    nums2 = [2, 3, 0, 1, 4]
    print("Input:", nums2)
    print("Minimum jumps required:", solution.jump(nums2))
    # Expected Output: 2
