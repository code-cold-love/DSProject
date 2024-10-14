#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 77. 组合 https://leetcode.cn/problems/combinations/
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 返回范围 [1, n] 中所有可能的 k 个数的组合
        # 1 <= k <= n
        ans, path = [], []

        def backtrack(n: int, k: int, start: int):
            if len(path) == k:  # 终止条件
                ans.append(path[:])
                return
            for i in range(start, n + 1):  # 选择本层集合中元素
                path.append(i)  # 处理节点
                backtrack(n, k, i + 1)  # 递归
                path.pop()  # 回溯，撤销处理的节点

        backtrack(n, k, 1)
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.combine(1, 1))  # [[1]]
    print(obj.combine(4, 2))  # [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
