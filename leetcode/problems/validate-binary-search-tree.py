#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 98. 验证二叉搜索树 https://leetcode.cn/problems/validate-binary-search-tree/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 判断 root 中序遍历下，输出的是不是有序序列
        vec = []

        def inorder(node: Optional[TreeNode]):
            if not node:
                return
            inorder(node.left)
            vec.append(node.val)
            inorder(node.right)

        inorder(root)
        for i in range(1, len(vec)):
            if vec[i] <= vec[i - 1]:  # 二叉搜索树中不能有重复元素
                return False
        return True


if __name__ == '__main__':
    head = TreeNode(2)
    head.left = TreeNode(1)
    head.right = TreeNode(3)
    print(Solution().isValidBST(head))  # True
