#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 104. 二叉树的最大深度 https://leetcode.cn/problems/maximum-depth-of-binary-tree/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        return max(left_height, right_height) + 1


if __name__ == '__main__':
    obj = Solution()
    node = TreeNode(3)
    node.left = TreeNode(9)
    node.right = TreeNode(20)
    node.right.left = TreeNode(15)
    node.right.right = TreeNode(7)
    print(obj.maxDepth(node))  # 3
