#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 160. 相交链表 https://leetcode.cn/problems/intersection-of-two-linked-lists/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # m 为链表 A 的长度，n 为链表 B 的长度
        # m + n = n + m，题目保证没有环
        if headA is None or headB is None:
            return None
        pa, pb = headA, headB
        while pa != pb:
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next
        return pa
