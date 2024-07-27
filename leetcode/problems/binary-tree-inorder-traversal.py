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
        ans, stk = [], []
        if root:
            stk.append(root)
        while stk:
            node = stk.pop()
            if node is None:  # 只有遇到空节点的时候，才将下一个节点放进结果集
                node = stk.pop()  # 重新取出栈中元素
                ans.append(node.val)  # 加入到结果集中
            else:
                if node.right:  # 添加右节点
                    stk.append(node.right)
                stk.append(node)  # 添加中节点
                stk.append(None)  # 中节点访问过，但还没有处理，加入空值作为标记
                if node.left:  # 添加左节点
                    stk.append(node.left)
        return ans


if __name__ == '__main__':
    obj = Solution()
    head = TreeNode(1)
    head.right = TreeNode(2)
    head.right.left = TreeNode(3)
    print(obj.inorderTraversal_recursion(head))  # [1, 3, 2]
    print(obj.inorderTraversal_iteration(head))  # [1, 3, 2]
