# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:
# Input: head = [1], n = 1
# Output: []

# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        list = []
        while head.next:
            list.append(head.val)
            head = head.next
        list.append(head.val)
        list.pop(-n)
        head = ListNode(list[0])
        current = head
        for i in range(1, len(list)):
            current.next = ListNode(list[i])
            current = current.next
        return head
    

    
def print_list(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()

# Örnek bir linked list oluştur
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Test için çıktıyı yazdır
print("Başlangıçtaki linked list:")
print_list(head)

# Solution sınıfını kullanarak belirli bir indexteki elemanı kaldır
sol = Solution()
new_head = sol.removeNthFromEnd(head, 2)

# Sonucu yazdır
print("Eleman çıkarıldıktan sonraki linked list:")
print_list(new_head)