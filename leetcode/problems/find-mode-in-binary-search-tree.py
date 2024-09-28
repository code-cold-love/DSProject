#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 501. 二叉搜索树中的众数 https://leetcode.cn/problems/find-mode-in-binary-search-tree/
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # 含有重复值的 BST
        stk, ans = [], []
        cur, pre = root, None
        cnt, max_cnt = 0, 0
        while cur or stk:
            if cur:
                stk.append(cur)
                cur = cur.left  # 左
            else:
                cur = stk.pop()
                if not pre:  # 第一个节点
                    cnt = 1
                elif pre.val == cur.val:
                    cnt += 1
                else:  # 与前一个节点的数值不同
                    cnt = 1
                if cnt == max_cnt:
                    ans.append(cur.val)
                elif cnt > max_cnt:
                    max_cnt = cnt
                    ans.clear()
                    ans.append(cur.val)
                pre = cur
                cur = cur.right  # 右
        return ans


if __name__ == '__main__':
    head = TreeNode(1)
    head.right = TreeNode(2)
    head.right.left = TreeNode(2)
    print(Solution().findMode(head))
