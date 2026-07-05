# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevGroup = dummy
        start = dummy.next

        while start:
            end = prevGroup
            for _ in range(k):
                end = end.next
                if not end:
                    return dummy.next
            if end:
                nextGroup = end.next

            prev = nextGroup
            curr = start
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            prevGroup.next = prev
            prevGroup = start
            start = nextGroup
        return dummy.next
            