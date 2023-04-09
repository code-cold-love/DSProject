# -*- coding: utf-8 -*-
# 19. 删除链表的倒数第 N 个结点 https://leetcode.cn/problems/remove-nth-node-from-end-of-list/
from typing import Optional


class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> Optional[ListNode]:
        if not head or n < 1:
            return head
        dummy = ListNode(0, head)  # 哑节点
        quick, slow = head, dummy
        for i in range(n):  # 快指针领先慢指针 n 个节点
            quick = quick.next
        while quick:
            quick = quick.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
