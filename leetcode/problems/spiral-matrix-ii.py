#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 59. 螺旋矩阵 II https://leetcode.cn/problems/spiral-matrix-ii/
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]

        idx = 1
        left, right = 0, n - 1
        upper, lower = 0, n - 1
        ans = [[-1] * n for _ in range(n)]
        while True:
            for i in range(left, right + 1):  # 从左到右
                ans[upper][i] = idx
                idx += 1
            upper += 1
            if upper > lower:
                break

            for i in range(upper, lower + 1):  # 从上到下
                ans[i][right] = idx
                idx += 1
            right -= 1
            if right < left:
                break

            for i in range(right, left - 1, -1):  # 从右到左
                ans[lower][i] = idx
                idx += 1
            lower -= 1
            if lower < upper:
                break

            for i in range(lower, upper - 1, -1):  # 从下到上
                ans[i][left] = idx
                idx += 1
            left += 1
            if left > right:
                break
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.generateMatrix(1))  # [[1]]
    print(solution.generateMatrix(3))  # [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
