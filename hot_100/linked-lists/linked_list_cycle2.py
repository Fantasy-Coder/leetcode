from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#哈希表
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        while head:
            if head in seen:
                return head
            seen.add(head)
            head = head.next
        return None
#快慢指针
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        while True:
            if not (fast and fast.next):
                return
            fast, slow = fast.next.next, slow.next
            #如果快慢指针相遇，说明链表有环，此时f = 2s,s = a + nb a为链表头到环入口的距离，b为环的长度，n为快指针在环内转了多少圈
            if fast == slow:
                break
        #当快慢指针相遇时，快指针已经在环内转了n圈，此时我们让快指针回到链表头，慢指针保持在相遇点，然后快慢指针以相同的速度前进，当它们再次相遇时，相遇点就是环的入口    
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast 