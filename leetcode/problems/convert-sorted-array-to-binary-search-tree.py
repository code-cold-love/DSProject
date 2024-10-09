#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 108. 将有序数组转换为二叉搜索树 https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left: int, right: int) -> Optional[TreeNode]:
            if left > right:  # 左闭右闭情况下的递归终止条件
                return None
            mid = left + (right - left) // 2  # 分割点
            # Python 表达式 left + (right - left) >> 1 中，+ 的运算优先级大于 >>，即 [left + (right - left)] >> 1
            node = TreeNode(nums[mid])
            node.left = helper(left, mid - 1)
            node.right = helper(mid + 1, right)
            return node

        root = helper(0, len(nums) - 1)
        return root
