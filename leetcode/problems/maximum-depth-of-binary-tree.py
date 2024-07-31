#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 104. 二叉树的最大深度 https://leetcode.cn/problems/maximum-depth-of-binary-tree/
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 层序遍历，迭代解法
        # 找出给定二叉树的最大深度（根节点到最远叶子节点的最长路径上的节点数）
        ans = 0
        if not root:
            return ans
        dq = deque([root])
        while dq:
            ans += 1
            level_size = len(dq)  # 当前层中节点个数
            for _ in range(level_size):
                curr = dq.popleft()
                if curr.left:
                    dq.append(curr.left)
                if curr.right:
                    dq.append(curr.right)
        return ans


if __name__ == '__main__':
    obj = Solution()
    node = TreeNode(3)
    node.left = TreeNode(9)
    node.right = TreeNode(20)
    node.right.left = TreeNode(15)
    node.right.right = TreeNode(7)
    print(obj.maxDepth(node))  # 3
