# Given a string s of lower and upper case English letters.
# A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:
# 0 <= i <= s.length - 2
# s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
# To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.
# Return the string after making it good. The answer is guaranteed to be unique under the given constraints.
# Notice that an empty string is also good.

# Example 1:
# Input: s = "leEeetcode"
# Output: "leetcode"
# Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".

# Example 2:
# Input: s = "abBAcC"
# Output: ""
# Explanation: We have many possible scenarios, and all lead to the same answer. For example:
# "abBAcC" --> "aAcC" --> "cC" --> ""
# "abBAcC" --> "abBA" --> "aA" --> ""

# Example 3:
# Input: s = "s"
# Output: "s"

class Solution(object):
    def makeGood(self, s):
            s = list(s)
            a = len(s) - 2
            while a >= 0:
                if (s[a].isupper() and s[a].lower() == s[a+1]) or (s[a].islower() and s[a].upper() == s[a+1]):
                    del s[a]
                    del s[a]
                    a = min(a+1, len(s)-2)
                else:
                    a -= 1
            return ''.join(s)
    
#test case
t = Solution()
print(t.makeGood("leEeetcode")) #"leetcode"
print(t.makeGood("abBAcC")) #""
print(t.makeGood("s")) #"s"
