# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def recursiveFunc(self, head):
        # base case
        if head is None or head.next is None:
            return head
        # recursive step 
        new_head = self.recursiveFunc(head.next)
        head.next.next = head
        head.next = None
        return new_head

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # recursion
        head = self.recursiveFunc(head)
        return head
        


        