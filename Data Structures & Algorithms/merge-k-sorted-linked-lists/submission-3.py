# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                merged.append(self.mergeTwoLists(lists[i],
                lists[i + 1] if len(lists) > i + 1 else None))
            lists = merged
        return lists[0]
    
    def mergeTwoLists(self, list1, list2):
        head = ListNode()
        curr = head
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        if list1 is not None:
            curr.next = list1
        if list2 is not None:
            curr.next = list2
        return head.next