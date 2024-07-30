#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 116. 填充每个节点的下一个右侧节点指针 https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/
from collections import deque
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, _next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = _next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # 给定一个完美二叉树，所有叶子节点都在同一层，每个父节点有两个子节点
        # 填充它的每个 next 指针，让这个指针指向其下一个右侧节点
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
