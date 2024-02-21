#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 144. 二叉树的前序遍历 https://leetcode.cn/problems/binary-tree-preorder-traversal/
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """递归"""
        ans = []

        def preorder(node: TreeNode):
            if not node:
                return
            ans.append(node.val)
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ans

    def preorderTraversal_stk(self, root: Optional[TreeNode]) -> List[int]:
        """迭代"""
        ans = []
        if not root:
            return ans
        stk, node = [], root
        while stk or node:
            while node:
                ans.append(node.val)
                stk.append(node)
                node = node.left  # 最左边
            node = stk.pop()
            node = node.right
        return ans


if __name__ == '__main__':
    obj = Solution()
    head = TreeNode(1)
    head.right = TreeNode(2)
    head.right.left = TreeNode(3)
    print(obj.preorderTraversal(head))  # [1, 2, 3]
    print(obj.preorderTraversal_stk(head))  # [1, 2, 3]
