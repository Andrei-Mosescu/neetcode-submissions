# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        next = head.next
        prev = head
        head.next = None
        while next is not None:
            nextn = next.next
            next.next = prev
            prev= next
            next = nextn
        return prev
        