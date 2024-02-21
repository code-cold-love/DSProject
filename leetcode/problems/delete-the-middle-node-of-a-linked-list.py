#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2095. 删除链表的中间节点 https://leetcode.cn/problems/delete-the-middle-node-of-a-linked-list/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        prev, fast = ListNode(0, head), head
        while fast and fast.next:
            fast = fast.next.next
            prev = prev.next
        prev.next = prev.next.next
        return head


if __name__ == '__main__':
    obj = Solution()
    node = ListNode(1)
    node.next = ListNode(3)
