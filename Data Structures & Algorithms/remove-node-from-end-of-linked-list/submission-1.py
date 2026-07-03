# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        for _ in range(n):
            if first:
                first = first.next
        
        dummy = ListNode(0, head)
        second = dummy

        while first and second:
            first = first.next
            second = second.next
        if second and second.next:
            second.next = second.next.next
        return dummy.next