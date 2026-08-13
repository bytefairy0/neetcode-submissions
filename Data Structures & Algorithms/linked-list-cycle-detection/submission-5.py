# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # edge cases
        if head is None or head.next is None or head.next.next is None:
            return False
        elif head.next.val == head.val:
            return True
        slowP = head
        fastP = head.next.next

        while fastP:
            if fastP.next is None:
                return False
            if fastP.next.val == slowP.val or fastP.val == slowP.val:
                return True
            slowP = slowP.next
            fastP = fastP.next.next

        return False