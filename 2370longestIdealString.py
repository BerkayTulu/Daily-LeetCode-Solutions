# You are given a string s consisting of lowercase letters and an integer k. We call a string t ideal if the following conditions are satisfied:

# t is a subsequence of the string s.
# The absolute difference in the alphabet order of every two adjacent letters in t is less than or equal to k.
# Return the length of the longest ideal string.

# A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

# Note that the alphabet order is not cyclic. For example, the absolute difference in the alphabet order of 'a' and 'z' is 25, not 1.

 

# Example 1:

# Input: s = "acfgbd", k = 2
# Output: 4
# Explanation: The longest ideal string is "acbd". The length of this string is 4, so 4 is returned.
# Note that "acfgbd" is not ideal because 'c' and 'f' have a difference of 3 in alphabet order.
# Example 2:

# Input: s = "abcd", k = 3
# Output: 4
# Explanation: The longest ideal string is "abcd". The length of this string is 4, so 4 is returned.

class Solution(object):
    def longestIdealString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        dp = [[0] * 26 for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(26):
                dp[i][j] = dp[i - 1][j] + (s[i - 1] == chr(ord('a') + j))
        res = 0
        for i in range(1, n + 1):
            for j in range(26):
                if dp[i][j] == 0:
                    continue
                for l in range(j + 1, 26):
                    if dp[i][l] - dp[i][j] <= k:
                        res = max(res, dp[i][l] - dp[i][j] + 1)
        return res