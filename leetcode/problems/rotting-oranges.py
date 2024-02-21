#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 994. 腐烂的橘子 https://leetcode.cn/problems/rotting-oranges/
from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def neighbors(x, y) -> (int, int):
            for dx, dy in ((r - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)):
                if 0 <= dx < m and 0 <= dy < n:
                    yield dx, dy

        m, n = len(grid), len(grid[0])
        q = deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
        d = 0
        while q:
            r, c, d = q.popleft()
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    q.append((nr, nc, d + 1))
        if any(1 in row for row in grid):
            return -1
        return d


if __name__ == '__main__':
    obj = Solution()
    print(obj.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))  # 4
