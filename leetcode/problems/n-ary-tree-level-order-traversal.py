#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 429. N 叉树的层序遍历 https://leetcode.cn/problems/n-ary-tree-level-order-traversal/
from collections import deque
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: Node) -> List[List[int]]:
        # 自顶向下遍历
        ans = []
        if not root:
            return ans
        dq = deque([root])
        while dq:
            level = []
            level_size = len(dq)  # 当前层二叉树节点的数量
            for _ in range(level_size):
                cur = dq.popleft()
                level.append(cur.val)
                for child in cur.children:  # 遍历当前节点所有孩子节点
                    dq.append(child)
            ans.append(level)
        return ans


if __name__ == '__main__':
    solution = Solution()
    head = Node(1)
    head.children = [Node(3), Node(2), Node(4)]
    print(solution.levelOrder(head))  # [[1], [3, 2, 4]]
