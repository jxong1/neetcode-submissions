# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        count = 1
        while curr:
            count += 1
            curr = curr.next
        target = count - n
        count = 1
        prev = None
        curr = head
        while count != target:
            count += 1
            prev = curr
            curr = curr.next
        if prev == None:
            return head.next if head.next else None
        else:
            prev.next = curr.next
            return head


        
        