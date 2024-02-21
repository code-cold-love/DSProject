#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 206. 反转链表 https://leetcode.cn/problems/reverse-linked-list/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next


class Solution:
    def reverseList_recursion(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """递归"""
        if not head or not head.next:
            return head
        new_node = self.reverseList_recursion(head.next)
        head.next.next = head
        head.next = None
        return new_node

    def reverseList_iteration(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """迭代"""
        pre = None
        cur = head
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        return pre


if __name__ == '__main__':
    obj = Solution()
    node = ListNode(1)
    node.next = ListNode(2)
    obj.reverseList_recursion(node)
