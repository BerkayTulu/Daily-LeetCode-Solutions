# You are given two linked lists: list1 and list2 of sizes n and m respectively.
# Remove list1's nodes from the ath node to the bth node, and put list2 in their place.
# The blue edges and nodes in the following figure indicate the result:
# Build the result list and return its head.
 
# Example 1:
# Input: list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
# Output: [10,1,13,1000000,1000001,1000002,5]
# Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.

# Example 2:
# Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
# Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
# Explanation: The blue edges and nodes in the above figure indicate the result.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        dummy = ListNode(0, list1)
        curr = dummy
        for _ in range(a):
            curr = curr.next
        start = curr
        for _ in range(b - a + 1):
            curr = curr.next
        end = curr.next
        start.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = end
        return dummy.next
# Time: O(n)
# Space: O(1)
# Difficulty: medium
def print_list(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()

# Test case
list1 = ListNode(10, ListNode(1, ListNode(13, ListNode(6, ListNode(9, ListNode(5))))))
a = 3
b = 4
list2 = ListNode(1000000, ListNode(1000001, ListNode(1000002)))
sol = Solution()
result = sol.mergeInBetween(list1, a, b, list2)

print_list(result)
# Output: 10 1 13 1000000 1000001 1000002 5
    

