#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 106. 从中序与后序遍历序列构造二叉树 https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """inorder 和 postorder 都由不同的值组成"""

        def helper(in_left: int, in_right: int) -> Optional[TreeNode]:
            # 如果这里没有节点构造二叉树了，就结束
            if in_left > in_right:
                return None

            # 选择 postorder_idx 位置的元素作为当前子树根节点
            val = postorder.pop()
            root = TreeNode(val)

            # 根据 root 所在位置分成左右两棵子树
            delimiter = idx_map[val]
            # 构造右子树
            root.right = helper(delimiter + 1, in_right)
            # 构造左子树
            root.left = helper(in_left, delimiter - 1)
            return root

        # 建立（元素，下标）键值对的哈希表
        # 题目规定 inorder 和 postorder 都由不同的值组成
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)
