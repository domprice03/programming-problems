# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tortoise = head
        hare = head

        while hare != None and hare.next != None:
            tortoise = tortoise.next
            hare = hare.next.next

            if tortoise == hare:
                return True

        return False