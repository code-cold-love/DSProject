#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 113. 路径总和 II https://leetcode.cn/problems/path-sum-ii/
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse(self, node: Optional[TreeNode], count: int, path: List[int], ans: List[List[int]]):
        if not node:
            return
        path.append(node.val)
        count -= node.val
        if not node.left and not node.right and count == 0:
            # ans.append(path[:])
            ans.append(path.copy())  # 注意，因为下面有 path.pop() 操作，所以这里不能直接存储 path 本身
        self.traverse(node.left, count, path, ans)
        self.traverse(node.right, count, path, ans)
        path.pop()

    def pathSum(self, root: Optional[TreeNode], target_sum: int) -> List[List[int]]:
        # 本题要遍历整个树，找到所有路径，所以递归方法中函数不要返回值
        # https://www.programmercarl.com/0112.%E8%B7%AF%E5%BE%84%E6%80%BB%E5%92%8C.html#%E6%80%9D%E8%B7%AF
        ans = []
        self.traverse(root, target_sum, [], ans)
        return ans


if __name__ == '__main__':
    head = TreeNode(5)
    head.left = TreeNode(4)
    head.right = TreeNode(8)
    head.left.left = TreeNode(11)
    head.left.left.right = TreeNode(2)
    head.right.right = TreeNode(4)
    head.right.right.left = TreeNode(5)
    print(Solution().pathSum(head, 22))  # [[5, 4, 11, 2], [5, 8, 4, 5]]
