#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 226. 翻转二叉树 https://leetcode.cn/problems/invert-binary-tree/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 把每个节点的左右孩子翻转一下，就可以达到整体翻转的效果
        # return self.recursion(root)
        return self.iteration(root)

    def recursion(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """递归，前序遍历解法"""
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.recursion(root.left)
        self.recursion(root.right)
        return root

    def iteration(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """迭代解法"""
        if not root:
            return root
        stk = [root]
        while stk:
            node = stk.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stk.append(node.left)
            if node.right:
                stk.append(node.right)
        return root
