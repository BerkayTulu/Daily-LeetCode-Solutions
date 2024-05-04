# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

# Example 1:
# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

# Example 2:
# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

class Solution(object):
    def findMaxLength(self, nums):
        max_length = 0
        count = 0
        sum_index = {0: -1}
        for i in range(len(nums)):
            count += 1 if nums[i] == 1 else -1
            if count in sum_index:
                max_length = max(max_length, i - sum_index[count])
            else:
                sum_index[count] = i
        return max_length

# test the solution
s = Solution()
nums = [0,1]
print(s.findMaxLength(nums)) # 2
nums = [0,1,0]
print(s.findMaxLength(nums)) # 2
nums = [0,0,1,0,0,0,1,1]
print(s.findMaxLength(nums)) # 6