# Given a string s of '(' , ')' and lowercase English characters.
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
# Formally, a parentheses string is valid if and only if:
# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
 
# Example 1:
# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

# Example 2:
# Input: s = "a)b(c)d"
# Output: "ab(c)d"

# Example 3:
# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.
 
# class Solution(object):
#     def minRemoveToMakeValid(self, s):
#         s = list(s)
#         a = 0
#         b = 0
#         for i in range(len(s)):
#             if s[i] == '(':
#                 a += 1
#             elif s[i] == ')':
#                 if a > 0:
#                     a -= 1
#                 else:
#                     s[i] = ''
#         for i in range(len(s)-1, -1, -1):
#             if s[i] == '(' and b > 0:
#                 s[i] = ''
#                 b -= 1
#             elif s[i] == '(':
#                 s[i] = ''
#             elif s[i] == ')':
#                 b += 1
#         return ''.join(s)
class Solution(object):
    def minRemoveToMakeValid(self, s):
        stack = []
        to_remove = set()

        for i, char in enumerate(s):
            if char not in "()":
                continue
            if char == '(':
                stack.append(i)
            elif not stack:
                to_remove.add(i)
            else:
                stack.pop()

        to_remove = to_remove.union(set(stack))
        return ''.join([char for i, char in enumerate(s) if i not in to_remove])
#test case
t = Solution()
print(t.minRemoveToMakeValid("lee(t(c)o)de)")) #"lee(t(c)o)de"
print(t.minRemoveToMakeValid("a)b(c)d")) #"ab(c)d"
print(t.minRemoveToMakeValid("))((")) #""
print(t.minRemoveToMakeValid("a)b(c)d")) #"ab(c)d"