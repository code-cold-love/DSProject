#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 117. 填充每个节点的下一个右侧节点指针 II https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, _next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = _next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        dq = deque([root])
        while dq:
            level_size = len(dq)
            prev = None
            for i in range(level_size):
                curr = dq.popleft()
                # 在单层遍历时记录本层的头部节点，然后在遍历时让前一个节点指向头部节点
                if prev:
                    prev.next = curr

                prev = curr
                if curr.left:
                    dq.append(curr.left)
                if curr.right:
                    dq.append(curr.right)
        return root
