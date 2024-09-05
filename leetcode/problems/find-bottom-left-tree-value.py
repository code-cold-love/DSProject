#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 513. 找树左下角的值 https://leetcode.cn/problems/find-bottom-left-tree-value/
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans = 0
        dq = deque([root])
        while dq:
            level_size = len(dq)
            for i in range(level_size):
                cur_node = dq.popleft()
                if i == 0:
                    ans = cur_node.val
                if cur_node.left:
                    dq.append(cur_node.left)
                if cur_node.right:
                    dq.append(cur_node.right)
        return ans


if __name__ == '__main__':
    head = TreeNode(2)
    head.left = TreeNode(1)
    head.right = TreeNode(3)
    print(Solution().findBottomLeftValue(head))  # 1
