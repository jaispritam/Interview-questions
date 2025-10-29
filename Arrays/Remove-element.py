# 27. Leetcode
# Remove Element

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Removes all occurrences of `val` from `nums` in-place and returns
        the count of elements not equal to `val`.

        Args:
            nums (List[int]): Input list of integers.
            val (int): Value to remove from the list.

        Returns:
            int: Number of elements remaining after removal (k).

        Example:
            >>> nums = [3, 2, 2, 3]
            >>> k = Solution().removeElement(nums, 3)
            >>> k, nums[:k]
            (2, [2, 2])
        """
        k = 0
        for num in nums:
            if num != val:
                nums[k] = num
                k += 1
        return k


if __name__ == "__main__":
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    sol = Solution()
    k = sol.removeElement(nums, val)
    print(f"After removal: {nums[:k]}, Count: {k}")
