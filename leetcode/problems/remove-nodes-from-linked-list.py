#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2487. 从链表中移除节点 https://leetcode.cn/problems/remove-nodes-from-linked-list/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next


class Solution:
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        while head is not None:
            p = head
            head = head.next
            p.next = dummy.next
            dummy.next = p
        return dummy.next

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.reverse(head)
        p = head
        while p.next is not None:
            if p.val > p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return self.reverse(head)


if __name__ == '__main__':
    obj = Solution()
    node = ListNode(5)
    node.next = ListNode(2)
    node.next.next = ListNode(13)
    node.next.next.next = ListNode(3)
    node.next.next.next.next = ListNode(8)
    node = obj.removeNodes(node)
    ans = []
    while node is not None:
        ans.append(node.val)
        node = node.next
    print(ans)
