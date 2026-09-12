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
        # edge case
        if not head:
            return None
        addresses = {}
        t1 = head
        newList = Node(head.val)
        t2 = newList
        addresses[t1] = t2

        # Create copy with nexts and store their respective addresses
        while t1.next:
            nextCopy = Node(t1.next.val)
            t2.next = nextCopy

            addresses[t1.next] = t2.next

            t1 = t1.next
            t2 = t2.next

        # now get addresses of randoms and point them accordingly 
        t1 = head
        t2 = newList
        while t1:
            if not t1.random:
                t2.random = None
            elif t1.random in addresses:
                    t2.random = addresses[t1.random]
            t1 = t1.next
            t2 = t2.next

        return newList

            

