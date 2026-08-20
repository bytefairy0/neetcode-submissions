# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # using stack
        if not head or not head.next:
            return

        # push all nodes in stack
        stack = []
        temp = head
        while temp:
            stack.append(temp)
            temp = temp.next

        # reorder only half
        n = len(stack)
        curr = head
        for _ in range(n//2):
            temp = curr.next
            curr.next = stack.pop()
            curr.next.next = temp
            curr = temp

        curr.next = None
        
        
            