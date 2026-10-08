# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        first = None
        n1, n2 = list1, list2
        if n1.val < n2.val:
            first = n1
            n1 = n1.next
        else:
            first = n2
            n2 = n2.next
        curr = first
        while n1 is not None or n2 is not None:
            if n1 is None:
                curr.next = n2
                break
            if n2 is None:
                curr.next = n1
                break
            if n1.val < n2.val:
                curr.next = n1
                curr = n1
                n1 = n1.next
            else:
                curr.next = n2
                curr = n2
                n2 = n2.next
            
        return first