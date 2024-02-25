#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 235. 二叉搜索树的最近公共祖先 https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @staticmethod
    def get_path(root: TreeNode, target: TreeNode) -> List[TreeNode]:
        """二叉搜索树遍历"""
        path = list()
        node = root
        while node != target:
            path.append(node)
            if target.val < node.val:
                node = node.left
            else:
                node = node.right
        path.append(node)
        return path

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        path_p = self.get_path(root, p)
        path_q = self.get_path(root, q)
        ancestor = None
        for u, v in zip(path_p, path_q):
            if u == v:
                ancestor = u
            else:  # 遇到的第一个分歧点
                break

        return ancestor


if __name__ == '__main__':
    obj = Solution()
