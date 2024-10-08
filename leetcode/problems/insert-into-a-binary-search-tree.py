#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 701. 二叉搜索树中的插入操作 https://leetcode.cn/problems/insert-into-a-binary-search-tree/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST_recursion(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # 输入数据保证，新值 val 和原始 BST 中的任意节点值都不同
        # 遍历 BST，找到空节点、插入元素即可
        if not root:
            return TreeNode(val)

        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        return root

    def insertIntoBST_iteration(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:  # 若根节点为空，则创建新节点并作为根节点返回
            return TreeNode(val)
        curr, parent = root, None
        while curr:
            parent = curr
            if curr.val > val:
                curr = curr.left
            else:
                curr = curr.right

        node = TreeNode(val)
        if val < parent.val:
            parent.left = node
        else:
            parent.right = node
        return root
