from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curA = headA
        curB = headB

        while curA:
            curB = headB

            while curB:
                if curA == curB:
                    return curA
                curB = curB.next
        
            curA = curA.next
         
        return None