#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 559. N 叉树的最大深度 https://leetcode.cn/problems/maximum-depth-of-n-ary-tree/
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: Node) -> int:
        # 层序遍历，迭代解法
        ans = 0
        if not root:
            return ans
        dq = deque([root])
        while dq:
            ans += 1
            level_size = len(dq)  # 当前层二叉树节点的数量
            for _ in range(level_size):
                curr = dq.popleft()
                if curr.children:
                    for child in curr.children:
                        dq.append(child)
        return ans


if __name__ == '__main__':
    solution = Solution()
    node = Node(1)
    node.children = [Node(3), Node(2), Node(4)]
    node.children[0].children = [Node(5), Node(6)]
    print(solution.maxDepth(node))  # 3
