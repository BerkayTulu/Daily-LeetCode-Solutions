# A wonderful string is a string where at most one letter appears an odd number of times.

# For example, "ccjjc" and "abab" are wonderful, but "ab" is not.
# Given a string word that consists of the first ten lowercase English letters ('a' through 'j'), return the number of wonderful non-empty substrings in word. If the same substring appears multiple times in word, then count each occurrence separately.

# A substring is a contiguous sequence of characters in a string.

 

# Example 1:

# Input: word = "aba"
# Output: 4
# Explanation: The four wonderful substrings are underlined below:
# - "aba" -> "a"
# - "aba" -> "b"
# - "aba" -> "a"
# - "aba" -> "aba"
# Example 2:

# Input: word = "aabb"
# Output: 9
# Explanation: The nine wonderful substrings are underlined below:
# - "aabb" -> "a"
# - "aabb" -> "aa"
# - "aabb" -> "aab"
# - "aabb" -> "aabb"
# - "aabb" -> "a"
# - "aabb" -> "abb"
# - "aabb" -> "b"
# - "aabb" -> "bb"
# - "aabb" -> "b"
# Example 3:

# Input: word = "he"
# Output: 2
# Explanation: The two wonderful substrings are underlined below:
# - "he" -> "h"
# - "he" -> "e"

class Solution(object):
    def wonderfulSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        # Initialize the result
        res = 0
        # Initialize the prefix sum
        prefix = [0] * 1024
        # Initialize the prefix sum at 0
        prefix[0] = 1
        # Initialize the mask
        mask = 0
        # Iterate the word
        for c in word:
            # Get the index
            index = ord(c) - ord('a')
            # Update the mask
            mask ^= 1 << index
            # Update the result
            res += prefix[mask]
            # Iterate the prefix
            for i in range(10):
                # Update the result
                res += prefix[mask ^ (1 << i)]
            # Update the prefix
            prefix[mask] += 1
        # Return the result
        return res