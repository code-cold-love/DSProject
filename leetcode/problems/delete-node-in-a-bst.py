#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 450. 删除二叉搜索树中的节点 https://leetcode.cn/problems/delete-node-in-a-bst/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # 节点数的范围 [0, 10**4]，节点值唯一
        if not root:  # 遍历到节点为空，直接返回
            return root
        if root.val == key:  # 找到要删除的节点
            # 1. 要删除的节点为叶子节点，直接删除节点，返回 Null 为根节点
            if not root.left and not root.right:
                return None
            # 2. 删除节点的左孩子为空，右孩子不为空，删除该节点后右孩子补位，返回右孩子为根节点
            elif not root.left:
                return root.right
            # 3. 删除节点的右孩子为空，左孩子不为空，删除该节点后左孩子补位
            elif not root.right:
                return root.left
            # 4. 左右孩子节点都不为空
            else:
                # 找到右子树中的最左节点
                cur = root.right
                while cur.left:
                    cur = cur.left
                # 将删除节点的左子树头结点（左孩子）放到删除节点的右子树最左节点的左孩子上
                cur.left = root.left
                return root.right  # 返回删除节点右孩子为新的根节点
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root
