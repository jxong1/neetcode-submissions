# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def dfs(node1, node2, carry):
            if node1 is None or node2 is None:
                if node1:
                    node2 = ListNode()
                elif node2:
                    node1 = ListNode()
                elif carry == 0:
                    return None
                else:
                    return ListNode(carry)

            val1, val2 = node1.val, node2.val
            val = val1 + val2 + carry
            r = val % 10
            q = val // 10
            new = ListNode(r)
            new.next = dfs(node1.next, node2.next, q)
            return new

        return dfs(l1, l2, 0)