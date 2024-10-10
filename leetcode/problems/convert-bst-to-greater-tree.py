#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 538. 把二叉搜索树转换为累加树 https://leetcode.cn/problems/convert-bst-to-greater-tree/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 树中所有的值互不相同，每个节点的值介于 -10**4 和 10**4 之间
        if not root:
            return root
        ans, stk = [], []
        cur, pre = root, 0
        # BST 中累加的顺序是右中左
        while cur or stk:
            if cur:
                stk.append(cur)
                cur = cur.right  # 向右
            else:
                cur = stk.pop()  # 中
                cur.val += pre
                pre = cur.val
                cur = cur.left  # 向左
        return root
