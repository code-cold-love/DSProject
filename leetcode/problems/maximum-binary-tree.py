#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 654. 最大二叉树 https://leetcode.cn/problems/maximum-binary-tree/
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # 1 <= nums.length <= 1000, 0 <= nums[i] <= 1000
        # 递归终止条件
        if not nums:
            return None

        # 找到数组中最大的值和对应下标
        max_val = max(nums)
        max_idx = nums.index(max_val)
        node = TreeNode(max_val)

        # 最大值所在的下标左区间，构造左子树
        node.left = self.constructMaximumBinaryTree(nums[:max_idx])
        # 最大值所在的下标右区间，构造右子树
        node.right = self.constructMaximumBinaryTree(nums[max_idx + 1:])
        return node
