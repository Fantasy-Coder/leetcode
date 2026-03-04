# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #如果一个为空，则返回另一个
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        #哑节点，避免了处理头节点为空的情况
        dummy = ListNode(0)
        #进位数
        carry = 0
        #p与dummy指向相同
        p = dummy
        #如果两个数都不为空，则相加，并更新进位数
        while l1 and l2:
            #相加，并将结果的个位数作为当前节点的值
            p.next = ListNode((l1.val + l2.val + carry)%10)
            #计算进位
            carry = (l1.val + l2.val + carry)//10
            #指向下一个节点
            p = p.next
            l1 = l1.next
            l2 = l2.next
        #若其中一个为空，则将另一个数的剩余部分与进位数相加，并更新进位数
        if l2:
            while l2:
                p.next = ListNode((l2.val + carry)%10)
                carry = (l2.val + carry)//10
                p = p.next
                l2 = l2.next
        if l1:
            while l1:
                p.next = ListNode((l1.val + carry)%10)
                carry = (l1.val + carry)//10
                p = p.next
                l1 = l1.next
        #若进位不为0，则增加一个节点为1。因为carry只为0和1，也可写为if carry == 1。
        if carry != 0:
            p.next = ListNode(1)
        #返回哑节点的下一个节点，即结果链表的头节点
        return dummy.next
