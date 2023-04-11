# -*- coding: utf-8 -*-
# 695. 岛屿的最大面积 https://leetcode.cn/problems/max-area-of-island/
from typing import List
from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        m, n = len(grid), len(grid[0])  # m 行 n 列
        for i in range(m):
            for j in range(n):
                area = 0
                q = deque([(i, j)])
                while q:
                    cur_i, cur_j = q.popleft()
                    if cur_i < 0 or cur_j < 0 or cur_i >= m or cur_j >= n or grid[cur_i][cur_j] != 1:
                        continue
                    area += 1
                    grid[cur_i][cur_j] = 0  # 每次经过一块土地时，将这块土地的值置为 0，确保每块土地访问不超过一次
                    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        next_i, next_j = cur_i + di, cur_j + dj
                        q.append((next_i, next_j))
                max_area = max(area, max_area)
        return max_area


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
