# Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
# The following rules define a valid string:
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 
# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "(*)"
# Output: true

# Example 3:
# Input: s = "(*))"
# Output: true

class Solution(object):
    def checkValidString(self, s):
        left = 0
        right = 0
        for i in range(len(s)):
            if s[i] in '(*':
                left += 1
            else:
                left -= 1
            if s[~i] in '*)':
                right += 1
            else:
                right -= 1
            if left < 0 or right < 0:
                return False
        return True
    
s = Solution()
print(s.checkValidString("()")) # True
print(s.checkValidString("(*)")) # True
print(s.checkValidString("(*))")) # True
print(s.checkValidString("(*)))")) # False
print(s.checkValidString("(*))")) # True
print(s.checkValidString("(*)))")) # False