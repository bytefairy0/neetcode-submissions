# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # MORE EFFICENT O(1) space {why i coulnt think of-}

        # find middle - using fast/slow ptr approach
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next

        # reverse the last half
        prev, curr = None, slow.next
        slow.next = None # disconnect 1st half
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # merge the two lists
        first, last = head, prev
        while last:
            tmp1, tmp2 = first.next, last.next

            first.next = last
            last.next = tmp1
            first = tmp1
            last = tmp2

        
            