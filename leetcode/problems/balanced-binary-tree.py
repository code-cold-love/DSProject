#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 110. 平衡二叉树 https://leetcode.cn/problems/balanced-binary-tree/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_height(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        left = self.get_height(node.left)
        right = self.get_height(node.right)
        if left == -1 or right == - 1 or abs(left - right) > 1:
            return -1  # 不平衡
        return max(left, right) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.get_height(root) != -1


if __name__ == '__main__':
    solution = Solution()
    node = TreeNode(3)
    node.left = TreeNode(9)
    node.right = TreeNode(20)
    node.right.left = TreeNode(15)
    node.right.right = TreeNode(7)
    print(solution.isBalanced(node))  # True
