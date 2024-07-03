#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 142. 环形链表 II https://leetcode.cn/problems/linked-list-cycle-ii/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 假如有环，则 slow 和 fast 的相遇点到入环点的距离，加上 n-1 圈的环长，恰好等于从链表头部到入环点的距离
        slow, fast = head, head
        while fast:
            slow = slow.next
            if not fast.next:
                return None
            fast = fast.next.next
            if slow == fast:
                ptr = head
                while ptr != slow:
                    ptr = ptr.next
                    slow = slow.next
                return ptr
        return None
