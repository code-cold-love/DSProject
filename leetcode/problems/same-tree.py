#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 100. 相同的树 https://leetcode.cn/problems/same-tree/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 递归解法
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == '__main__':
    solution = Solution()
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)
    tree2 = TreeNode(1)
    tree2.left = TreeNode(2)
    tree2.right = TreeNode(3)
    print(solution.isSameTree(tree1, tree2))  # True
