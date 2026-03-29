from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        
        carry = 0
        dummy = ListNode(0)
        p = dummy
        while l1 and l2:
            p.next = ListNode((l1.val + l2.val + carry) %10)
            carry = (l1.val + l2.val + carry) // 10
            p = p.next
            l1 =l1.next  
            l2 = l2.next      
        while l1:
            p.next = ListNode((l1.val + carry) %10)
            carry = (l1.val + carry) // 10
            p = p.next
            l1 = l1.next
        while l2:
            p.next = ListNode((l2.val + carry) % 10)
            carry = (l2.val + carry) // 10
            p = p.next
            l2 = l2.next
        if carry != 0:
            p.next = ListNode(1)
        return dummy.next