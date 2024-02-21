#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1637. 两点之间不包含任何点的最宽垂直区域 https://leetcode.cn/problems/widest-vertical-area-between-two-points-containing-no-points/
from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # 2 <= len(points) <= 10**5
        # len(points[i]) == 2
        points.sort(key=lambda k: k[0])
        return max(points[i][0] - points[i - 1][0] for i in range(len(points) - 1))


if __name__ == '__main__':
    obj = Solution()
    print(obj.maxWidthOfVerticalArea([[8, 7], [9, 9], [7, 4], [9, 7]]))  # 1
    print(obj.maxWidthOfVerticalArea([[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]))  # 3
