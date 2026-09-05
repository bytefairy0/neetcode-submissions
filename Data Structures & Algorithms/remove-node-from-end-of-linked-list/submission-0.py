# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # count len of list
        temp = head
        l = 0
        while temp:
            l += 1
            temp = temp.next

        print("l: ", l)

        # Edge cases
        if n == l: # remove 1st node
            head = head.next
            return head

        temp = head
        for _ in range(1, l-n):
            temp = temp.next # the previous node to be removed

        temp.next = temp.next.next

        return head
