# -*- coding: utf-8 -*-
# 617. 合并二叉树 https://leetcode.cn/problems/merge-two-binary-trees/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        elif not root2:
            return root1
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1


if __name__ == '__main__':
    obj = Solution()
    root_1 = TreeNode(1)
    root_1.left = TreeNode(3)
    root_1.right = TreeNode(2)
    root_1.left.right = TreeNode(5)
    root_2 = TreeNode(2)
    root_2.left = TreeNode(1)
    root_2.right = TreeNode(3)
    root_2.left.right = TreeNode(4)
    root_2.right.right = TreeNode(7)
    merge_root = obj.mergeTrees(root_1, root_2)  # [3, 4, 5, 5, 4, null, 7]
