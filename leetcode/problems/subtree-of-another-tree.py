#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 572. 另一棵树的子树 https://leetcode.cn/problems/subtree-of-another-tree/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 以 p 和 q 为根节点的两棵二叉树是否相同
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        elif not root or not subRoot:
            return False
        return self.isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right,
                                                                                                      subRoot)


if __name__ == '__main__':
    solution = Solution()
    node1 = TreeNode(3)
    node1.left = TreeNode(4)
    node1.right = TreeNode(5)
    node1.left.left = TreeNode(1)
    node1.left.right = TreeNode(2)
    node2 = TreeNode(4)
    node2.left = TreeNode(1)
    node2.right = TreeNode(2)
    print(solution.isSubtree(node1, node2))  # True
