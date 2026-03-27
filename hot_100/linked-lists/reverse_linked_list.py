from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#双指针
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur , pre = head , None
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre
    
#平行赋值 双指针
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur , pre = head , None
        while cur:
            cur.next , pre , cur = pre ,cur ,cur.next
        return pre

#递归
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recur(cur ,pre):
            if not cur:
                return pre
            res = recur(cur.next, cur)
            cur.next = pre
            return res
        return recur(head, None)