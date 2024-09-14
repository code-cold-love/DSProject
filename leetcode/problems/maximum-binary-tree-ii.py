#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 998. 最大二叉树 II https://leetcode.cn/problems/maximum-binary-tree-ii/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # 树中节点数目在 [1, 100] 内，树中的所有值互不相同
        # 最大树定义：一棵树，满足每个节点的值都大于其子树中的任何其他值
        parent, curr = None, root
        while curr:
            if val > curr.val:
                if not parent:  # 此时 curr 为根节点
                    # 根节点的值小于 val，新的树以 val 作为根节点，原来的树作为左子树
                    return TreeNode(val, root, None)
                node = TreeNode(val, curr, None)
                parent.right = node
                return root
            else:
                # 由于 val 是新添加的位于数组末尾的元素，那么在构造的结果中，val 一定出现在偏右的位置
                parent = curr
                curr = curr.right
        # 遍历完成后，仍然没有找到比 val 值更小的节点
        parent.right = TreeNode(val)
        return root
