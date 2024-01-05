# -*- coding: utf-8 -*-
# 64. 最小路径和 https://leetcode.cn/problems/minimum-path-sum/
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 动态规划，直接修改原矩阵减少空间复杂度
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if i == 0 and j >= 1:  # 第一行只能从左往右走
                    grid[i][j] += grid[i][j - 1]
                elif j == 0 and i >= 1:  # 第一列只能从上往下走
                    grid[i][j] += grid[i - 1][j]
                elif i > 0 and j > 0:
                    grid[i][j] += min(grid[i][j - 1], grid[i - 1][j])
        return grid[-1][-1]


if __name__ == '__main__':
    obj = Solution()
    print(obj.minPathSum([[1, 2, 3], [4, 5, 6]]))  # 12
    print(obj.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))  # 7
