#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 637. 二叉树的层平均值 https://leetcode.cn/problems/average-of-levels-in-binary-tree/
from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        if not root:
            return ans
        dq = deque([root])
        while dq:
            # 层序遍历时把每一层求个总和，再取该层平均值
            level_sum = 0
            level_size = len(dq)
            for i in range(level_size):
                cur = dq.popleft()
                level_sum += cur.val
                if cur.left:
                    dq.append(cur.left)
                if cur.right:
                    dq.append(cur.right)
            ans.append(level_sum / level_size)
        return ans


if __name__ == '__main__':
    solution = Solution()
    head = TreeNode(3)
    head.left = TreeNode(9)
    head.right = TreeNode(20)
    head.right.left = TreeNode(15)
    head.right.right = TreeNode(7)
    print(solution.averageOfLevels(head))  # [3.0, 14.5, 11.0]
