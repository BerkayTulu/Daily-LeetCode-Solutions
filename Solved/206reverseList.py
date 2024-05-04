# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
# Input: head = [1,2]
# Output: [2,1]

# Example 3:
# Input: head = []
# Output: []
 
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev

# Time: O(n)
# Space: O(1)
# Difficulty: easy
    
def print_list(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()

# Test case
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
sol = Solution()
result = sol.reverseList(head)

print_list(result)
# Output: 5 4 3 2 1

# Test case
head = ListNode(1, ListNode(2))
sol = Solution()
result = sol.reverseList(head)

print_list(result)
# Output: 2 1

# Test case
head = ListNode()
sol = Solution()
result = sol.reverseList(head)

print_list(result)

# Output:
