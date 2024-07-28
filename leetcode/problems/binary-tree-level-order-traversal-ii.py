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
        # 自底向上遍历
        ans = []
        if not root:
            return ans
        dq = deque([root])
        while dq:
            level = []
            for _ in range(len(dq)):
                cur = dq.popleft()
                level.append(cur.val)
                if cur.left:
                    dq.append(cur.left)
                if cur.right:
                    dq.append(cur.right)
            ans.append(level)
        return ans[::-1]  # 反转


if __name__ == '__main__':
    solution = Solution()
    head = TreeNode(3)
    head.left = TreeNode(9)
    head.right = TreeNode(20)
    head.right.left = TreeNode(15)
    head.right.right = TreeNode(7)
    print(solution.levelOrderBottom(head))  # [[15, 7], [9, 20], [3]]
