# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        fast = curr
        head = None
        count = 1
        prev = None
        while fast or count == k:
            if count == k:
                if head == None:
                    head = fast
                if fast:
                    nxt = fast.next
                    fast.next = None
                tail = self.reverseList(curr)
                tail.next = nxt

                if prev:
                    prev.next = fast

                prev = tail
                curr = nxt
                fast = nxt
            else:
                fast = fast.next
            count = count % k + 1
            if fast is None:
                break
        return head

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev = None
        curr = head
        while curr.next:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        curr.next = prev
        return head