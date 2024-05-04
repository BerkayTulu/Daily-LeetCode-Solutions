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
        dp = [0] * 26
    
    # Iterate over each character in the string
        for c in s:
            # Get the index of the current character
            index = ord(c) - ord('a')
            
            # Calculate the current max length for this character
            max_len = 0
            
            # Check all possible characters within the distance k
            for i in range(max(0, index - k), min(25, index + k) + 1):
                max_len = max(max_len, dp[i])
            
            # Update dp for the current character
            dp[index] = max_len + 1
        
        # The result is the maximum value in dp, which gives us the length of the longest ideal subsequence
        return max(dp)

