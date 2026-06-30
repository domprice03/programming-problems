# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tortoise = head
        hare = head

        while tortoise != None and hare != None:
            tortoise = tortoise.next
            hare = hare.next
            if hare is None:
                break
            hare = hare.next

            if tortoise == hare:
                return True

        return False