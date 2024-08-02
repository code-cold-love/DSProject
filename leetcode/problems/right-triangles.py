#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 3128. 直角三角形 https://leetcode.cn/problems/right-triangles/
from typing import List


class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        ans = 0
        col_sums = [sum(col) - 1 for col in zip(*grid)]
        for row in grid:
            row_sum = sum(row) - 1
            ans += row_sum * sum(col_sum for x, col_sum in zip(row, col_sums) if x)
        return ans
