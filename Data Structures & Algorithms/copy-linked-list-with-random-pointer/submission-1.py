"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        curr = head
        m = {}
        while curr:
            copy = Node(curr.val)
            m[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = m[curr]
            copy.next = m.get(curr.next)
            copy.random = m.get(curr.random)
            curr = curr.next
        return m[head]