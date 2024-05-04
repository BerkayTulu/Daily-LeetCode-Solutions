# Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

# Example 1:
# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 6
# Explanation: The maximal rectangle is shown in the above picture.

# Example 2:
# Input: matrix = [["0"]]
# Output: 0

# Example 3:
# Input: matrix = [["1"]]
# Output: 1

class Solution(object):
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        m = len(matrix)
        n = len(matrix[0])

        left = [0] * n
        right = [n] * n
        height = [0] * n

        max_area = 0

        for i in range(m):
            current_left, current_right = 0, n
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0

            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], current_left)
                else:
                    left[j] = 0
                    current_left = j + 1

            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], current_right)
                else:
                    right[j] = n
                    current_right = j

            for j in range(n):
                max_area = max(max_area, (right[j] - left[j]) * height[j])

        return max_area
    
# test case
s = Solution()
print(s.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])) # 6
print(s.maximalRectangle([["0"]])) # 0
print(s.maximalRectangle([["1"]])) # 1
print(s.maximalRectangle([["0","0"]])) # 0
print(s.maximalRectangle([["0","1"]])) # 1
print(s.maximalRectangle([["1","0"]])) # 1
print(s.maximalRectangle([["1","1"]])) # 2
print(s.maximalRectangle([["1","1"],["1","1"]])) # 4