# 80. Leetcode
# Remove Duplicates from Sorted Array II

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Question:
        Given a sorted integer array `nums`, remove duplicates in-place such that
        each unique element appears at most **twice**. Return the count `k` of valid elements.

        Example:
        Input:  nums = [1,1,1,2,2,3]
        Output: k = 5, nums = [1,1,2,2,3,_]

        Explanation:
        - We can allow each number to appear at most twice.
        - Use a pointer `k` to track where the next valid number should be placed.
        - Start `k` from 2 (since first two elements are always valid).
        - Iterate through the array from index 2 onward:
            - If the current number `nums[i]` is not equal to the element at `nums[k-2]`
              (i.e., not forming a third duplicate), copy it to `nums[k]` and increment `k`.
        - Return `k` as the number of elements kept.

        Time Complexity:  O(n)
        Space Complexity: O(1)
        """

        if len(nums) <= 2:
            return len(nums)

        k = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1

        return k
