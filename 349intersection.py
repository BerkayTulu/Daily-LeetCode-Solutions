# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
 
# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.

class Solution(object):
    def intersection(self, nums1, nums2):
        intersec = set(nums1) & set(nums2)
        return intersec

sol = Solution()
# Test Case 1
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
expected_output = [2]
print(sol.intersection(nums1, nums2))

# Test Case 2
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
expected_output = [9, 4]
print(sol.intersection(nums1, nums2))

# Test Case 3
nums1 = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9, 10]
expected_output = []
print(sol.intersection(nums1, nums2))

# Test Case 4
nums1 = [1, 2, 3, 4, 5]
nums2 = [5, 4, 3, 2, 1]
expected_output = [1, 2, 3, 4, 5]
print(sol.intersection(nums1, nums2))

# Test Case 5
nums1 = []
nums2 = []
expected_output = []
print(sol.intersection(nums1, nums2))


        