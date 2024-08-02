#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 101. 对称二叉树 https://leetcode.cn/problems/symmetric-tree/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def compare(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        # 排除空节点的情况
        if not left and right:
            return False
        elif left and not right:
            return False
        elif not left and not right:
            return True
        elif left.val != right.val:
            return False
        outside = self.compare(left.left, right.right)  # 比较外侧
        inside = self.compare(left.right, right.left)  # 比较里侧
        return outside and inside

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 比较左右子树的里侧和外侧元素是否相等
        # 一个树的遍历顺序是左、右、中，另一个树的遍历顺序是右、左、中
        if not root:
            return True
        return self.compare(root.left, root.right)


if __name__ == '__main__':
    solution = Solution()
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(2)
    head.left.left = TreeNode(3)
    head.left.right = TreeNode(4)
    head.right.left = TreeNode(4)
    head.right.right = TreeNode(3)
    print(solution.isSymmetric(head))  # True
