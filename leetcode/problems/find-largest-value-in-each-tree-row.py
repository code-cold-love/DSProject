#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 515. 在每个树行中找最大值 https://leetcode.cn/problems/find-largest-value-in-each-tree-row/
from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # 二叉树的层序遍历解法
        ans = []
        if not root:
            return ans
        dq = deque([root])
        while dq:
            max_val = float('-inf')
            level_size = len(dq)  # 当前层二叉树节点的数量
            for _ in range(level_size):
                cur = dq.popleft()
                max_val = max(max_val, cur.val)
                if cur.left:
                    dq.append(cur.left)
                if cur.right:
                    dq.append(cur.right)
            ans.append(max_val)
        return ans


if __name__ == '__main__':
    solution = Solution()
    head = TreeNode(1)
    head.left = TreeNode(3)
    head.left.left = TreeNode(5)
    head.left.right = TreeNode(3)
    head.right = TreeNode(2)
    head.right.right = TreeNode(9)
    print(solution.largestValues(head))  # [1, 3, 9]
