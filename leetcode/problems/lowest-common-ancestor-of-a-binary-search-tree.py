#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 235. 二叉搜索树的最近公共祖先 https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ancestor = root
        while True:
            if ancestor.val > p.val and ancestor.val > q.val:
                ancestor = ancestor.left
            elif ancestor.val < p.val and ancestor.val < q.val:
                ancestor = ancestor.right
            else:  # 遇到分岔点，此时 p 和 q 要么在当前节点的不同子树中，要么其中一个就是当前节点
                break
        return ancestor

    def lowestCommonAncestor_recursion(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root.val > p.val and root.val > q.val:  # p 和 q 都在左子树
            return self.lowestCommonAncestor_recursion(root.left, p, q)
        if root.val < p.val and root.val < q:  # p 和 q 都在右子树
            return self.lowestCommonAncestor_recursion(root.right, p, q)
        return root  # 其他，此时 p 和 q 要么在当前节点的不同子树中，要么其中一个就是当前节点
