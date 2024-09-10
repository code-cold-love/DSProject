#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 105. 从前序与中序遍历序列构造二叉树 https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(in_left: int, in_right: int) -> Optional[TreeNode]:
            if in_left > in_right:
                return None
            # 选择 pre_idx 位置的元素作为当前子树根节点
            val = preorder.popleft()
            root = TreeNode(val)

            # 根据 root 所在位置分成左右两棵子树
            delimiter = idx_map[val]
            root.left = helper(in_left, delimiter - 1)
            root.right = helper(delimiter + 1, in_right)
            return root

        preorder = deque(preorder)
        # 建立（元素，下标）键值对的哈希表
        # 题目规定 preorder 和 inorder 均无重复元素
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)


if __name__ == '__main__':
    solution = Solution()
    print(solution.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))
