#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 112. 路径总和 https://leetcode.cn/problems/path-sum/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse(self, node: TreeNode, count: int) -> bool:
        """
        回溯
        :param node: 本题递归终止条件是判断叶子节点，所以递归过程中不传空节点
        :param count: 计数器，初始为目标和，每次减去遍历路径节点上的数值
        :return:
        """
        # 递归终止条件
        if not node:
            return False
        if not node.left and not node.right:
            return True if count == 0 else False

        # return self.traverse(node.left, count-node.left) or self.traverse(node.right, count-node.right)  # 隐含回溯逻辑
        if node.left:
            count -= node.left.val  # 递归，处理节点
            if self.traverse(node.left, count):
                return True
            count += node.left.val  # 回溯，撤销处理结果
        if node.right:
            count -= node.right.val  # 递归，处理节点
            if self.traverse(node.right, count):
                return True
            count += node.right.val  # 回溯，撤销处理结果
        return False

    def hasPathSum(self, root: Optional[TreeNode], target_sum: int) -> bool:
        # 判断树中是否存在从根节点到叶子节点的路径，满足路径上所有节点值相加等于 target_sum
        if not root:
            return False
        return self.traverse(root, target_sum - root.val)

    def hasPathSum_iteration(self, root: Optional[TreeNode], target_sum: int) -> bool:
        if not root:
            return False
        stk = [(root, root.val)]  # 本题要记录路径数值
        while stk:
            node, path_sum = stk.pop()
            if not node.left and not node.right and path_sum == target_sum:
                return True
            if node.left:
                stk.append((node.left, path_sum + node.left.val))
            if node.right:
                stk.append((node.right, path_sum + node.right.val))
        return False


if __name__ == '__main__':
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    print(Solution().hasPathSum_iteration(head, 5))  # False
