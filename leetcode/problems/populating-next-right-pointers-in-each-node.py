#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 116. 填充每个节点的下一个右侧节点指针 https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left=None, right=None, _next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = _next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        # 只能使用常量级额外空间
        # 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度
        node = root
        if node is None:
            return root
        while node.left:
            row_start = node
            row_start.left.next = row_start.right
            while row_start.next:
                row_start.right.next = row_start.next.left  # 右节点的 next 为相邻相隔的左节点
                row_start = row_start.next
                row_start.left.next = row_start.right
            node = node.left
        return root


if __name__ == '__main__':
    obj = Solution()
