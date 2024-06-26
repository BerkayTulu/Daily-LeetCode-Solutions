# You are given an integer array nums and a positive integer k.
# Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.
# A subarray is a contiguous sequence of elements within an array.

# Example 1:
# Input: nums = [1,3,2,3,3], k = 2
# Output: 6
# Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].

# Example 2:
# Input: nums = [1,4,2,1], k = 3
# Output: 0
# Explanation: No subarray contains the element 4 at least 3 times.

from collections import defaultdict


class Solution(object):
    def countSubArrays(self, nums, k):
        count = defaultdict(int)
        result = 0
        left = 0

        for right in range(len(nums)):
            count[nums[right]] += 1

            while count[nums[right]] >= k:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1

            result += left

        return result
 
# test the solution
s = Solution()
nums = [1,3,2,3,3]
k = 2
print(s.countSubArrays(nums, k)) # 6
nums = [1,4,2,1]
k = 3
print(s.countSubArrays(nums, k)) # 0