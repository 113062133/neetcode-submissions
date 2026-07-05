# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevGroup = dummy

        while True:
            end = prevGroup
            for _ in range(k):
                if end:
                    end = end.next
                else:
                    break
            
            if end:
                nextGroup = end.next
            else:
                break

            prev = nextGroup
            curr = prevGroup.next
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = prevGroup.next
            prevGroup.next = end
            prevGroup = temp
            
        return dummy.next
            