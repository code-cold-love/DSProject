#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 107. 二叉树的层序遍历 II https://leetcode.cn/problems/binary-tree-level-order-traversal-ii/
from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = list()
        if not root:
            return ret
        q = deque([root])
        while q:
            n, tmp = len(q), list()
            for _ in range(n):
                node = q.popleft()
                tmp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ret.append(tmp)
        return ret[::-1]


if __name__ == '__main__':
    obj = Solution()
    head = TreeNode(3)
    head.left = TreeNode(9)
    head.right = TreeNode(20)
    head.right.left = TreeNode(15)
    head.right.right = TreeNode(7)
    print(obj.levelOrderBottom(head))  # [[15, 7], [9, 20], [3]]
