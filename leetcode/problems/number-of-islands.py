#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 200. 岛屿数量 https://leetcode.cn/problems/number-of-islands/
from typing import List


class Solution:
    def __init__(self):
        self.grid = None
        self.rows = self.cols = 0
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(self, x: int, y: int):
        self.grid[x][y] = '0'
        for direction in self.directions:
            new_x, new_y = x + direction[0], y + direction[1]
            if 0 <= new_x < self.rows and 0 <= new_y < self.cols and self.grid[new_x][new_y] == '1':
                self.dfs(new_x, new_y)

    def numIslands(self, grid: List[List[str]]) -> int:
        land = 0
        self.grid = grid
        self.rows, self.cols = len(grid), len(grid[0])
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == '1':
                    land += 1
                    self.dfs(i, j)
        return land


if __name__ == '__main__':
    obj = Solution()
    print(obj.numIslands([['1', '1', '1', '1', '0'],
                          ['1', '1', '0', '1', '0'],
                          ['1', '1', '0', '0', '0'],
                          ['0', '0', '0', '0', '0']]))  # 1
    print(obj.numIslands([['1', '1', '0', '0', '0'],
                          ['1', '1', '0', '0', '0'],
                          ['0', '0', '1', '0', '0'],
                          ['0', '0', '0', '1', '1']]))  # 3
