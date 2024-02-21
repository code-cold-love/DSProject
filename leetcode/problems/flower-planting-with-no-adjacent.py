#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1042. 不邻接植花 https://leetcode.cn/problems/flower-planting-with-no-adjacent/
from typing import List


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        """邻接列表+颜色标记"""
        adj = [[] for i in range(n)]  # 整个图的邻接列表 adj
        for path in paths:
            x, y = path[0] - 1, path[1] - 1
            adj[x].append(y)
            adj[y].append(x)

        ans = [0] * n  # 初始时，将每个花园的颜色都标记为 0
        for i in range(n):
            colored = [False] * 5
            for vertex in adj[i]:
                colored[ans[vertex]] = True
            for j in range(1, 5):  # 从未被标记的颜色中找到一种颜色给当前的花园
                if colored[j] is False:
                    ans[i] = j
                    break
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.gardenNoAdj(3, [[1, 2], [2, 3], [3, 1]]))  # [1, 2, 3]
