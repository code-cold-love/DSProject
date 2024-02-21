#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 145. 二叉树的后序遍历 https://leetcode.cn/problems/binary-tree-postorder-traversal/
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """递归"""
        ans = []

        def postorder(node: TreeNode):
            if not node:
                return
            postorder(node.left)
            postorder(node.right)
            ans.append(node.val)

        postorder(root)
        return ans

    def postorderTraversal_stk(self, root: Optional[TreeNode]) -> List[int]:
        """迭代"""
        ans, stk = [], []
        prev = None
        while root or stk:
            while root:
                stk.append(root)
                root = root.left  # 一直往左下走
            root = stk.pop()
            if not root.right or root.right == prev:  # 没有右子树或者右子树已经遍历过
                ans.append(root.val)
                prev = root
                root = None
            else:
                stk.append(root)
                root = root.right
        return ans


if __name__ == '__main__':
    obj = Solution()
    head = TreeNode(1)
    head.right = TreeNode(2)
    head.right.left = TreeNode(3)
    print(obj.postorderTraversal(head))  # [3, 2, 1]
    print(obj.postorderTraversal_stk(head))  # [3, 2, 1]
