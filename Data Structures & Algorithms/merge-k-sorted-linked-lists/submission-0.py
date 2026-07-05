# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1

        if list1.val <= list2.val:
            head = list1
            temp1 = list1.next
            temp2 = list2
        else:
            head = list2
            temp1 = list1
            temp2 = list2.next
            
        curr = head
        while temp1 and temp2:
            if temp1.val <= temp2.val:
                curr.next = temp1
                temp1 = temp1.next
            else:
                curr.next = temp2
                temp2 = temp2.next
            curr = curr.next
        
        if temp1:
            curr.next = temp1
        elif temp2:
            curr.next = temp2
        return head

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is None:
            return None
        
        head = None
        for l in lists:
            head = self.mergeTwoLists(head, l)
        return head