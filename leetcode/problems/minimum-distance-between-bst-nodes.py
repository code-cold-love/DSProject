#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 783. 二叉搜索树节点最小距离 https://leetcode.cn/problems/minimum-distance-between-bst-nodes/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.pre = None
        self.ans = 2 * 10 ** 5 + 1

    def traverse(self, cur: Optional[TreeNode]) -> None:
        if not cur:
            return
        self.traverse(cur.left)  # 左
        if isinstance(self.pre, TreeNode):  # 中
            self.ans = min(self.ans, cur.val - self.pre.val)
        self.pre = cur
        self.traverse(cur.right)  # 右

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # BST 中节点的数目范围是 [2, 100]
        self.ans, self.pre = 2 * 10 ** 5 + 1, None
        self.traverse(root)
        return self.ans


if __name__ == '__main__':
    head = TreeNode(1)
    head.left = TreeNode(0)
    head.right = TreeNode(48)
    head.right.left = TreeNode(12)
    head.right.right = TreeNode(49)
    print(Solution().minDiffInBST(head))  # 1
