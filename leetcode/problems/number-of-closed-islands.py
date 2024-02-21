#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1254. 统计封闭岛屿的数目 https://leetcode.cn/problems/number-of-closed-islands/
from typing import List
from collections import deque


class Solution:
    def __init__(self):
        self.land = 0
        self.grid = None
        self.rows = self.cols = 0
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def dfs(self, x: int, y: int) -> bool:
        if x < 0 or y < 0 or x >= self.rows or y >= self.cols:
            return False
        elif self.grid[x][y] != 0:  # 某块陆地周围 (x, y) 处是水或者仍然是陆地
            return True
        self.grid[x][y] = -1
        res1, res2, res3, res4 = self.dfs(x - 1, y), self.dfs(x + 1, y), self.dfs(x, y - 1), self.dfs(x, y + 1)
        return res1 and res2 and res3 and res4

    def closedIsland_dfs(self, grid: List[List[int]]) -> int:
        # 深度有限搜索
        self.land = 0
        self.grid = grid
        self.rows, self.cols = len(self.grid), len(self.grid[0])
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == 0 and self.dfs(i, j):
                    self.land += 1
        return self.land

    def closedIsland(self, grid: List[List[int]]) -> int:
        # 广度有限搜索
        self.land = 0
        self.grid = grid
        self.rows, self.cols = len(self.grid), len(self.grid[0])
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == 0:
                    dq = deque([])
                    dq.append((i, j))
                    self.grid[i][j] = 1
                    closed = True
                    while dq:
                        x, y = dq.popleft()
                        if x == 0 or y == 0 or x == self.rows - 1 or y == self.cols - 1:  # 网格边缘处的陆地一定不封闭
                            closed = False
                        for direction in self.directions:
                            new_x, new_y = x + direction[0], y + direction[1]
                            if 0 <= new_x < self.rows and 0 <= new_y < self.cols and self.grid[new_x][new_y] == 0:
                                self.grid[new_x][new_y] = 1
                                dq.append((new_x, new_y))
                    if closed:
                        self.land += 1
        return self.land


if __name__ == '__main__':
    obj = Solution()
    print(obj.closedIsland([[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]))  # 1
    print(obj.closedIsland([[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0],
                            [1, 0, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0]]))  # 2
    print(obj.closedIsland_dfs([[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]))  # 1
    print(obj.closedIsland_dfs([[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0],
                            [1, 0, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0]]))  # 2
