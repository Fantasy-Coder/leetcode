# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#将两个链表的值存储在一个列表中，对列表进行排序，然后再创建一个新的链表
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        val = []
        while list1:
            val.append(list1.val)
            list1 = list1.next
        while list2:
            val.append(list2.val)
            list2 = list2.next
        val.sort()
        dummy = ListNode(0)
        cur = dummy
        for num in val:
            cur.next = ListNode(num)
            cur = cur.next
        return dummy.next
    

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 递归终止条件
        if not list1:
            return list2
        if not list2:
            return list1
        
        # 谁小就用谁当头，然后递归拼接 next
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2