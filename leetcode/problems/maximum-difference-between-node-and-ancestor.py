# -*- coding: utf-8 -*-
# 1026. 节点与其祖先之间的最大差值 https://leetcode.cn/problems/maximum-difference-between-node-and-ancestor/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        max_diff = 0

        def dfs(node: Optional[TreeNode]):
            if not node:
                return 0, 0
            elif not node.left and not node.right:
                return node.val, node.val
            nonlocal max_diff
            ret_mi, ret_ma = node.val, node.val
            if node.left:
                mi, ma = dfs(node.left)
                max_diff = max(max_diff, abs(node.val - mi), abs(node.val - ma))
                ret_mi = min(mi, ret_mi)
                ret_ma = max(ma, ret_ma)
            if node.right:
                mi, ma = dfs(node.right)
                max_diff = max(max_diff, abs(node.val - mi), abs(node.val - ma))
                ret_mi = min(mi, ret_mi)
                ret_ma = max(ma, ret_ma)
            return ret_mi, ret_ma

        dfs(root)
        return max_diff


if __name__ == '__main__':
    obj = Solution()
    head = TreeNode(1)
    head.right = TreeNode(2)
    head.right.right = TreeNode(0)
    head.right.right.left = TreeNode(3)
    print(obj.maxAncestorDiff(head))  # 3
