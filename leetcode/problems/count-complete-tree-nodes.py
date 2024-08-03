#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 222. 完全二叉树的节点个数 https://leetcode.cn/problems/count-complete-tree-nodes/
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        ans = 0
        if not root:
            return ans
        dq = deque([root])
        while dq:
            level_size = len(dq)
            ans += level_size
            for _ in range(level_size):
                curr = dq.popleft()
                if curr.left:
                    dq.append(curr.left)
                if curr.right:
                    dq.append(curr.right)
        return ans


if __name__ == '__main__':
    solution = Solution()
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.right = TreeNode(3)
    node.left.left = TreeNode(4)
    node.left.right = TreeNode(5)
    node.right.left = TreeNode(6)
    print(solution.countNodes(node))  # 6
