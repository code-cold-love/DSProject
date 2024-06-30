#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 203. 移除链表元素 https://leetcode.cn/problems/remove-linked-list-elements/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 0 <= val <= 50
        dummy = ListNode(-1, head)
        temp = dummy
        while dummy.next:
            if dummy.next.val == val:
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next
        return temp.next


if __name__ == '__main__':
    node = ListNode(7)
    node.next = ListNode(7)
    node.next.next = ListNode(7)
    node.next.next.next = ListNode(7)
    print(Solution().removeElements(node, 7))
