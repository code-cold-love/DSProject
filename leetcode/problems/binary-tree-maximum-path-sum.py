# -*- coding: utf-8 -*-
# 124. 二叉树中的最大路径和 https://leetcode.cn/problems/binary-tree-maximum-path-sum/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_val = 0

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.max_val = root.val  # 初始最大值就是根节点的值

        def dfs(node: Optional[TreeNode]):
            if not node:
                return 0
            # 分别递归遍历其左右子树可以为当前节点提供的收益
            left = max(0, dfs(node.left))  # 如果收益为负，那么宁可不要，置为 0
            right = max(0, dfs(node.right))
            self.max_val = max(self.max_val, node.val + left + right)
            return node.val + max(left, right)  # 每次递归返回的是当前节点可以为父节点提供的收益

        dfs(root)
        return self.max_val


if __name__ == '__main__':
    obj = Solution()
