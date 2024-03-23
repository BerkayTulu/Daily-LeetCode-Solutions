# You are given the head of a singly linked-list. The list can be represented as:
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.
# Example 1:
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]

# Example 2:
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def reorderList(self, head):
        if not head:
            return
        # Find the middle of the list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Reverse the second half of the list
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        # Merge the two halves
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
        return head
def printList(node):
    values = []
    while node:
        values.append(str(node.val))
        node = node.next
    print("->".join(values))
    
s = Solution()

# Test case 1
node4 = ListNode(4)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
print(s.reorderList(node1))  # Should print: 1->4->2->3

# Test case 2
node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
printList(s.reorderList(node1))  # Should print: 1->5->2->4->3

# Test case 3
node1 = ListNode(1)
printList(s.reorderList(node1))  # Should print: 1

# Test case 4
printList(s.reorderList(None)) # Should print: None
