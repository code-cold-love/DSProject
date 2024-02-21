#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1019. 链表中的下一个更大节点 https://leetcode.cn/problems/next-greater-node-in-linked-list/
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        """单调栈"""
        n, arr = 0, []
        stack = []  # 内部值非严格单调递减，栈中的元素对应“还没有找到下一个更大元素”的那些元素，这些元素在栈中的顺序与它们在链表中的顺序一致
        cur = head
        while cur:
            n += 1
            arr.append(cur.val)
            cur = cur.next
        ans = [0] * n
        for i in range(n):
            while stack and arr[i] > arr[stack[-1]]:
                idx = stack.pop()
                ans[idx] = arr[i]
            stack.append(i)
        return ans


if __name__ == '__main__':
    obj = Solution()
    node = ListNode(2)
    node.next = ListNode(1)
    node.next.next = ListNode(5)
    print(obj.nextLargerNodes(node))
