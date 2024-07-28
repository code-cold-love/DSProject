#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 199. 二叉树的右视图 https://leetcode.cn/problems/binary-tree-right-side-view/
from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # 在一棵二叉树的右侧，按照从顶部到底部的顺序，返回仅从右侧能看到的节点值
        ans = []
        if not root:
            return ans
        dq = deque([root])
        while dq:
            level_size = len(dq)
            for i in range(level_size):
                cur = dq.popleft()
                if i == level_size - 1:  # 当前层到最右边，从右侧只能看到当前值
                    ans.append(cur.val)
                if cur.left:
                    dq.append(cur.left)
                if cur.right:
                    dq.append(cur.right)
        return ans


if __name__ == '__main__':
    solution = Solution()
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.left.right = TreeNode(5)
    head.right = TreeNode(3)
    head.right.right = TreeNode(4)
    print(solution.rightSideView(head))  # [1, 3, 4]
