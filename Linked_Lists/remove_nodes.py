from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        cur = head

        while cur:
            if cur.val == val:
                prev.next = cur.next
                cur = prev.next
            else:
                prev = cur
                cur = cur.next

        if dummy.next:
            head = dummy.next
        else:
            head = None

        return head