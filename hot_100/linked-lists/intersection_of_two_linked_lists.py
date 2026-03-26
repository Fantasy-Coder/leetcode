from typing import Optional
#你走你的路，我走我的路；
#你走完了走我的路，我走完了走你的路；
#我们终会相遇 —— 要么在交点，要么在终点。
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A = headA
        B = headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A