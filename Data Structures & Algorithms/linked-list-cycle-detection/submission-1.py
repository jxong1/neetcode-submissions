# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        curr = head
        while curr.next:
            if curr.val == -999999:
                return True
            curr.val = -999999
            curr = curr.next
        return False