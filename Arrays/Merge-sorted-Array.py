# 88. Leetcode
# Merge Sorted Array


"""
Merge two sorted arrays in-place.

Problem:
Given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and integers m and n representing the number of valid elements in each,
merge them so that nums1 becomes a single sorted array in-place.

Example:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
"""

class Solution:
    def merge(self, nums1, m, nums2, n):
        for j in range(n):
            nums1[m + j] = nums2[j]
        nums1.sort()


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    Solution().merge(nums1, 3, nums2, 3)
    print(nums1)
