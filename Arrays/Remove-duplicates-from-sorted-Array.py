#27. Leetcode
# Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Question:
        Given a sorted integer array nums, remove duplicates in-place such that
        each unique element appears only once and returns the number of unique elements (k).

        Example:
        Input: nums = [0,0,1,1,1,2,2,3,3,4]
        Output: k = 5, nums = [0,1,2,3,4,_,_,_,_,_]

        Explanation:
        - The array is already sorted, so duplicates will be consecutive.
        - We use a pointer `index` to track the last position of a unique element.
        - Iterate through the array:
            - Whenever we find a new unique element (different from nums[index]),
              move it forward to nums[index + 1].
        - Return index + 1 as the total count of unique elements.
        """

        if not nums:
            return 0

        index = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[index]:
                index += 1
                nums[index] = nums[i]

        return index + 1
