# Given a positive integer n, find the pivot integer x such that:
# The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
# Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.

# Example 1:
# Input: n = 8
# Output: 6
# Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.

# Example 2:
# Input: n = 1
# Output: 1
# Explanation: 1 is the pivot integer since: 1 = 1.

# Example 3:
# Input: n = 4
# Output: -1
# Explanation: It can be proved that no such integer exist.

class Solution(object):
    def pivotInteger(self, n):
        l, r = 1, n
        while l <= r:
            p = (l + r) // 2
            l_sum =  (1 + p) / 2 * p
            r_sum = (p + n) / 2 * (n - p + 1) 
            if l_sum == r_sum:
                return p
            if l_sum > r_sum:
                r = p - 1
            else:
                l = p + 1
        return -1
    
    
    def testPivotInteger(self):
        assert self.pivotInteger(8) == 6
        assert self.pivotInteger(1) == 1
        assert self.pivotInteger(4) == -1

        print("All test cases pass")

sol = Solution()
sol.testPivotInteger()
