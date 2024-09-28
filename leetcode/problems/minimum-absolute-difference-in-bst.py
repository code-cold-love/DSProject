#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 530. 二叉搜索树的最小绝对差 https://leetcode.cn/problems/minimum-absolute-difference-in-bst/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stk, cur, pre, ans = [], root, None, float('inf')
        while cur or len(stk) > 0:
            if cur:
                stk.append(cur)
                cur = cur.left  # 左
            else:
                cur = stk.pop()
                if pre:  # 中
                    ans = min(ans, cur.val - pre.val)
                pre = cur
                cur = cur.right  # 右
        return ans


if __name__ == '__main__':
    head = TreeNode(4)
    head.left = TreeNode(2)
    head.right = TreeNode(6)
    head.left.left = TreeNode(1)
    head.left.right = TreeNode(3)
    print(Solution().getMinimumDifference(head))  # 1
