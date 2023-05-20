# -*- coding: utf-8 -*-
# 102. 二叉树的层序遍历 https://leetcode.cn/problems/binary-tree-level-order-traversal/
from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ret, q = [], deque()
        q.append(root)
        while q:
            n, tmp = len(q), []
            for i in range(n):
                node = q.popleft()
                tmp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ret.append(tmp)
        return ret


if __name__ == '__main__':
    obj = Solution()
    head = TreeNode(3)
    head.left = TreeNode(9)
    head.right = TreeNode(20)
    head.right.left = TreeNode(15)
    head.right.right = TreeNode(7)
    print(obj.levelOrder(head))  # [[3], [9, 20], [15, 7]]
