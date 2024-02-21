#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 695. 岛屿的最大面积 https://leetcode.cn/problems/max-area-of-island/
from typing import List
from collections import deque


class Solution:
    def __init__(self):
        self.max_area = 0

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.max_area = 0
        rows, cols = len(grid), len(grid[0])
        q = deque([])
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(x: int, y: int):
            area = 0
            q.append((x, y))
            while q:
                x, y = q.popleft()
                if (x, y) in visited:
                    continue
                area += 1
                visited.add((x, y))
                for direction in directions:
                    new_x, new_y = x + direction[0], y + direction[1]
                    if (new_x, new_y) in visited:
                        continue
                    elif 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] == 1:
                        q.append((new_x, new_y))
            self.max_area = max(area, self.max_area)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    bfs(i, j)
        return self.max_area


if __name__ == '__main__':
    obj = Solution()
    print(obj.maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]]))  # 0
    print(obj.maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                               [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                               [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))  # 6
