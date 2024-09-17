#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 700. 二叉搜索树中的搜索 https://leetcode.cn/problems/search-in-a-binary-search-tree/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST_recursion(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # root 是二叉搜索树，树中节点数在 [1, 5000] 范围内
        if not root or root.val == val:
            return root
        elif root.val > val:
            return self.searchBST_recursion(root.left, val)
        else:
            return self.searchBST_recursion(root.right, val)

    def searchBST_iteration(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # root 是二叉搜索树，树中节点数在 [1, 5000] 范围内
        while root:
            if val < root.val:
                root = root.left
            elif val > root.val:
                root = root.right
            else:
                return root
        return None
