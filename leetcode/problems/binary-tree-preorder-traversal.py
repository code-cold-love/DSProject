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
    def preorderTraversal_recursion(self, root: Optional[TreeNode]) -> List[int]:
        """递归"""
        ans = []

        def preorder(node: TreeNode):  # 确定递归函数的参数和返回值
            if not node:  # 递归终止条件
                return
            # 单层递归逻辑
            ans.append(node.val)
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ans

    def preorderTraversal_iteration(self, root: Optional[TreeNode]) -> List[int]:
        """迭代"""
        ans, stk = [], []
        if root:
            stk.append(root)
        while stk:
            node = stk.pop()
            if node is None:
                node = stk.pop()
                ans.append(node.val)
            else:
                if node.right:  # 右
                    stk.append(node.right)
                if node.left:  # 左
                    stk.append(node.left)
                stk.append(node)  # 中
                stk.append(None)  # 要处理的节点放入栈后，紧接着放入空值作为标记
        return ans


if __name__ == '__main__':
    obj = Solution()
    head = TreeNode(1)
    head.right = TreeNode(2)
    head.right.left = TreeNode(3)
    print(obj.preorderTraversal_recursion(head))  # [1, 2, 3]
    print(obj.preorderTraversal_iteration(head))  # [1, 2, 3]
