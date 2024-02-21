#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 463. 岛屿的周长 https://leetcode.cn/problems/island-perimeter/
from typing import List
from collections import deque


class Solution:
    def __init__(self):
        self.land = 0
        self.border = 0
        self.direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        self.land = self.border = 0

        def bfs(x, y):
            q = deque([])
            visited = set()
            q.append((x, y))
            while q:
                x, y = q.popleft()
                if (x, y) in visited:
                    continue
                self.land += 1
                visited.add((x, y))
                for direction in self.direction:
                    new_x, new_y = x + direction[0], y + direction[1]
                    if (new_x, new_y) in visited:
                        continue
                    elif 0 <= new_x < row and 0 <= new_y < col and grid[new_x][new_y] == 1:
                        q.append((new_x, new_y))
                        self.border += 1

        for i in range(row):
            flag = False
            for j in range(col):
                if grid[i][j] == 1:
                    bfs(i, j)
                    flag = True
                    break
            if flag:
                break

        return self.land * 4 - self.border * 2


if __name__ == '__main__':
    obj = Solution()
    print(obj.islandPerimeter([[1]]))  # 4
    print(obj.islandPerimeter([[1, 0]]))  # 4
    print(obj.islandPerimeter([[0], [1]]))  # 4
    print(obj.islandPerimeter([[1, 1], [1, 1]]))  # 8
    print(obj.islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))  # 16
