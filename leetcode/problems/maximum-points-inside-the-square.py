#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 3143. 正方形中的最多点数 https://leetcode.cn/problems/maximum-points-inside-the-square/
from math import inf
from typing import List


class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        # 本题中正方形的中心在 (0, 0)，所有的边都平行于坐标轴
        # 维护次小半径（正方形边长的一半）
        min1 = [inf] * 26  # min1[j] 为标签位 chr(j + 97) 的所有点到 (0, 0) 的最小切比雪夫距离
        min2 = inf  # min2 为次小切比雪夫距离中的最小值
        for i, c in enumerate(s):
            x, y = points[i]
            j = ord(c) - ord('a')
            distance = max(abs(x), abs(y))  # 点 (x, y) 到 (0, 0) 的切比雪夫距离
            if distance < min1[j]:
                # distance 是最小的，则 min1[j] 是次小的
                min2 = min(min2, min1[j])
                min1[j] = distance
            elif distance < min2:  # distance 是次小的
                min2 = distance
        return sum(d < min2 for d in min1)


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxPointsInsideSquare([[1, 1], [-2, -2], [-2, -2]], 'abb'))  # 1
