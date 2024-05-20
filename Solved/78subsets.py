# Given an integer array nums of unique elements, return all possible 
# subsets
#  (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]

class Solution:
    def subsets(self, nums):
        res = []
        def backtrack(start, path):
            res.append(path)
            for i in range(start, len(nums)):
                backtrack(i+1, path + [nums[i]])
        backtrack(0, [])
        return res

#test code
nums = [1,2,3]
sol = Solution()
print(sol.subsets(nums))
nums = [0]
print(sol.subsets(nums))
