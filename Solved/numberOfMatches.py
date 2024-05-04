# Example 1:

# Input: n = 7
# Output: 6
# Explanation: Details of the tournament: 
# - 1st Round: Teams = 7, Matches = 3, and 4 teams advance.
# - 2nd Round: Teams = 4, Matches = 2, and 2 teams advance.
# - 3rd Round: Teams = 2, Matches = 1, and 1 team is declared the winner.
# Total number of matches = 3 + 2 + 1 = 6.
# Example 2:

# Input: n = 14
# Output: 13
# Explanation: Details of the tournament:
# - 1st Round: Teams = 14, Matches = 7, and 7 teams advance.
# - 2nd Round: Teams = 7, Matches = 3, and 4 teams advance.
# - 3rd Round: Teams = 4, Matches = 2, and 2 teams advance.
# - 4th Round: Teams = 2, Matches = 1, and 1 team is declared the winner.
# Total number of matches = 7 + 3 + 2 + 1 = 13.
 

def makeMatch(n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
                return 0
        elif n % 2 == 0:
                return n // 2 + makeMatch(n//2)
        else:
                return (n - 1) // 2 + makeMatch((n - 1) // 2 + 1)

print(makeMatch(7))
print(makeMatch(14))