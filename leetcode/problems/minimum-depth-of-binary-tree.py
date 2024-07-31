#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 111. 二叉树的最小深度 https://leetcode.cn/problems/minimum-depth-of-binary-tree/
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # 找出给定二叉树的最小深度（最小深度是从根节点到最近叶子节点的最短路径上的节点数量）
        ans = 0
        if not root:
            return ans
        dq = deque([root])
        while dq:
            ans += 1
            level_size = len(dq)  # 当前层节点数
            for _ in range(level_size):
                curr = dq.popleft()
                if not curr.left and not curr.right:
                    # 当左右孩子节点都为空时，说明遍历到最低点了
                    return ans

                if curr.left:
                    dq.append(curr.left)
                if curr.right:
                    dq.append(curr.right)
        return ans


if __name__ == '__main__':
    solution = Solution()
    node = TreeNode(3)
    node.left = TreeNode(9)
    node.right = TreeNode(20)
    node.right.left = TreeNode(15)
    node.right.right = TreeNode(7)
    print(solution.minDepth(node))  # 2
