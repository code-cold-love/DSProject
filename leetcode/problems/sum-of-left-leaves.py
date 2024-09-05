#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 404. 左叶子之和 https://leetcode.cn/problems/sum-of-left-leaves/
from typing import Optional


# Definition for a binary tree head.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # 必须通过节点的【父节点】来判断其左孩子是不是左叶子
        # 递归终止条件
        if not root:  # 空节点的左叶子值一定是 0
            return 0
        elif not root.left and not root.right:  # 叶子节点的左叶子值也必定是 0
            return 0

        # 单层递归逻辑
        if root.left and not root.left.left and not root.left.right:  # 左子树就是一个左叶子
            left = root.left.val
        else:
            left = self.sumOfLeftLeaves(root.left)
        right = self.sumOfLeftLeaves(root.right)
        return left + right

    def sumOfLeftLeaves_iteration(self, root: Optional[TreeNode]) -> int:
        # 必须通过节点的父节点来判断其左孩子是不是左叶子
        if not root:  # 空节点的左叶子值一定是 0
            return 0
        stk = [root]
        ans = 0
        while stk:
            node = stk.pop()
            if node.left and not node.left.left and not node.left.right:  # 左子树就是一个左叶子
                ans += node.left.val
            if node.left:
                stk.append(node.left)
            if node.right:
                stk.append(node.right)
        return ans


if __name__ == '__main__':
    head = TreeNode(3)
    head.left = TreeNode(9)
    head.right = TreeNode(20)
    head.right.left = TreeNode(15)
    head.right.right = TreeNode(7)
    print(Solution().sumOfLeftLeaves(head))  # 24
