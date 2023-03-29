# -*- coding: utf-8 -*-
# 2596. 检查骑士巡视方案 https://leetcode.cn/problems/check-knight-tour-configuration/
from typing import List


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        # 在有效的巡视方案中，骑士会从棋盘的左上角 (0, 0) 出发，并且访问棋盘上的每个格子恰好一次
        # grid[row][col] 表示单元格 (row, col) 是骑士访问的第 grid[row][col] 个单元格
        # n = grid.length = grid[i].length
        # 3 <= n <= 7
        # 0 <= grid[row][col] < n * n，所有整数互不相同
        n = len(grid)
        pos = [0] * (n ** 2)
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                pos[val] = (i, j)  # 记录坐标
        if pos[0] != (0, 0):
            return False
        for t in range(n ** 2 - 1):
            (x1, y1), (x2, y2) = pos[t], pos[t + 1]
            dx, dy = abs(x2 - x1), abs(y2 - y1)  # 移动距离
            if (dx == 2 and dy == 1) or (dx == 1 and dy == 2):
                continue
            return False
        return True


if __name__ == '__main__':
    obj = Solution()
    print(obj.checkValidGrid([[0, 3, 6], [5, 8, 1], [2, 7, 4]]))  # False
    print(obj.checkValidGrid([[0, 11, 16, 5, 20], [17, 4, 19, 10, 15], [12, 1, 8, 21, 6], [3, 18, 23, 14, 9], [24, 13, 2, 7, 22]]))  # True
