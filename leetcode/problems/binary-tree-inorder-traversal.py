#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 94. 二叉树的中序遍历 https://leetcode.cn/problems/binary-tree-inorder-traversal/
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal_recursion(self, root: Optional[TreeNode]) -> List[int]:
        """递归"""
        ans = []

        def inorder(node: TreeNode) -> None:  # 确定递归函数的参数和返回值
            if not node:  # 递归终止条件
                return
            # 单层处理逻辑
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)

        inorder(root)
        return ans

    def inorderTraversal_iteration(self, root: Optional[TreeNode]) -> List[int]:
        """迭代"""
        ans = []
        if not root:
            return ans

        stk, node = [], root
        while stk or node:
            while node:
                stk.append(node)
                node = node.left  # 一直往左下走
            node = stk.pop()
            ans.append(node.val)  # 访问节点
            node = node.right  # 往右走
        return ans


if __name__ == '__main__':
    obj = Solution()
    head = TreeNode(1)
    head.right = TreeNode(2)
    head.right.left = TreeNode(3)
    print(obj.inorderTraversal_recursion(head))  # [1, 3, 2]
    print(obj.inorderTraversal_iteration(head))  # [1, 3, 2]
