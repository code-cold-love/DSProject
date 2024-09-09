#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2181. 合并零之间的节点 https://leetcode.cn/problems/merge-nodes-in-between-zeros/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = head
        curr = head.next
        while curr.next:
            if curr.val:  # 如果当前节点值不为 0
                tail.val += curr.val
            else:  # 如果当前节点值等于 0，则更新 tail 为 tail.next，然后把 tail.val 置为 0
                tail = tail.next
                tail.val = 0
            curr = curr.next
        tail.next = None
        return head
