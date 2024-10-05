#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 236. 二叉树的最近公共祖先 https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 所有节点的值都是唯一的
        # p、q 为不同节点且均存在于给定的二叉树中
        if root == q or root == p or not root:  # 终止条件
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 左右均有返回值，当前 root 即为祖先节点
        if left and right:
            return root
        if not left:  # left 为空，right 不为空
            return right
        return left
