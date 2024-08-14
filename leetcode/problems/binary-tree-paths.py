#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 257. 二叉树的所有路径 https://leetcode.cn/problems/binary-tree-paths/
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        stk, paths, ans = [root], [str(root.val)], []
        while stk:
            curr = stk.pop()
            path = paths.pop()
            if not (curr.left or curr.right):  # 当前节点为叶子节点
                ans.append(path)
            if curr.right:
                stk.append(curr.right)
                paths.append(path + '->' + str(curr.right.val))
            if curr.left:
                stk.append(curr.left)
                paths.append(path + '->' + str(curr.left.val))
        return ans


if __name__ == '__main__':
    solution = Solution()
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.right = TreeNode(3)
    node.left.right = TreeNode(5)
    print(solution.binaryTreePaths(node))  # ['1->2->5', '1->3']
