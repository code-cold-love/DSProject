#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 669. 修剪二叉树 https://leetcode.cn/problems/trim-a-binary-search-tree/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # 修剪二叉搜索树，使得所有节点值在 [low, high] 中
        if not root:  # 终止条件
            return

        # 单层递归逻辑
        if root.val < low:  # 当前节点的元素小于 low
            # 递归右子树，寻找符合区间 [low, high] 的节点
            return self.trimBST(root.right, low, high)
        elif root.val > high:  # 当前节点的元素大于 high
            # 递归左子树，寻找符合区间 [low, high] 的节点
            return self.trimBST(root.left, low, high)
        else:
            root.left = self.trimBST(root.left, low, high)  # root.left 接入符合条件的左孩子
            root.right = self.trimBST(root.right, low, high)  # root.right 接入符合条件的右孩子
            return root
