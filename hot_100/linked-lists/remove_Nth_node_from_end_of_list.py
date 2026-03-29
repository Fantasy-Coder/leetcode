from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#反转链表，删除后再反转
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 第一步：反转链表
        cur = head
        pre = None
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        
        # 第二步：删除反转后的【第n个节点】（原倒数第n个）
        dummy = ListNode(0)  # 加一个虚拟头，防止删第一个节点报错
        dummy.next = pre
        temp = dummy
        n1 = 0
        while temp.next:
            if n1 == n - 1:
                temp.next = temp.next.next
                break
            temp = temp.next
            n1 += 1
        
        # 第三步：再次反转回来
        cur = dummy.next
        pre = None
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre
    
#先计算链表长度，再删除倒数第n个节点
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def getLength(head:ListNode) -> int:
            # 计算链表长度
            length = 0
            while head:
                length += 1
                head = head.next
            return length
        #哑节点，防止删除第一个节点时出错
        dummy = ListNode(0,head)
        length = getLength(head)
        #cur指向要删除节点的前一个节点
        cur = dummy
        #length - n + 1是要删除节点的位置，循环length - n次后cur就指向要删除节点的前一个节点
        for i in range(1, length - n +1):
            cur = cur.next
        cur.next = cur.next.next
        # 返回新的头节点
        return dummy.next