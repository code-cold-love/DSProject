#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 3111. 覆盖所有点的最少矩阵数目 https://leetcode.cn/problems/minimum-rectangles-to-cover-points/
from typing import List


class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        # 0 <= xi == points[i][0] <= 10**9，0 <= yi == points[i][1] <= 10**9
        # 每个店都至少被一个矩形覆盖的前提下，最少需要多少个矩形
        # 矩形的高没有限制，矩形越宽，覆盖的点越多（矩形的宽度不超过 w）
        points.sort(key=lambda point: point[0])  # 横坐标按照从小到大的顺序排序
        ans = 0
        bound = -1  # 右边缘的横坐标，初始化时设为 -1
        for x, _ in points:
            if x > bound:  # 此时需要一个新的宽度为 w 的矩形来覆盖
                ans += 1
                bound = x + w  # 右边缘更新
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.minRectanglesToCoverPoints([[2, 3], [1, 2]], 0))  # 2
