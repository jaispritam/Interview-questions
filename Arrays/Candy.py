class Solution(object):
    def candy(self, ratings):
        """
        Problem:
        ----------
        Given an array 'ratings' representing the rating of each child standing in a line,
        distribute candies to each child such that:
          1. Every child gets at least one candy.
          2. A child with a higher rating gets more candies than their immediate neighbors.

        The goal is to find the minimum total number of candies required.

        Approach:
        ----------
        This problem is solved using a two-pass greedy approach:

        1. **Forward pass:** (Left → Right)
           - Ensure that each child with a higher rating than the left neighbor gets more candies.

        2. **Backward pass:** (Right → Left)
           - Ensure that each child with a higher rating than the right neighbor also gets more candies.
           - Use `max()` to avoid reducing candies assigned in the forward pass.

        3. Sum up the candies to get the total minimum required.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        n = len(ratings)               # Number of children
        candies = [1] * n              # Initialize each child with 1 candy

        # ---------- Forward Pass ----------
        # If the current child's rating is higher than the previous one,
        # give 1 more candy than the previous child.
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # ---------- Backward Pass ----------
        # If the previous child's rating is higher than the current one,
        # ensure the previous child has more candies than the current.
        cnt = 0
        for i in range(n - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                candies[i - 1] = max(candies[i - 1], candies[i] + 1)
            cnt += candies[i - 1]  # Add candies count progressively

        # Add the last child's candies and return total
        return cnt + candies[-1]
