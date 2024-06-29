#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 885. 螺旋矩阵 III https://leetcode.cn/problems/spiral-matrix-iii/
from typing import List


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ans = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 顺时针方向
        left, right, top, bottom = cStart - 1, cStart + 1, rStart - 1, rStart + 1  # 四个方向的边界
        x, y = rStart, cStart  # (x, y) 为当前节点
        cnt, direction = 1, 0
        while cnt <= rows * cols:
            if 0 <= x < rows and 0 <= y < cols:
                ans.append([x, y])  # (x, y) 在矩阵中
                cnt += 1
            if direction == 0 and y == right:  # 向右，到右边界
                direction += 1
                right += 1  # 右边界右移
            elif direction == 1 and x == bottom:  # 向下，到底边界
                direction += 1
                bottom += 1  # 底边界下移
            elif direction == 2 and y == left:  # 向左，到左边界
                direction += 1
                left -= 1  # 左边界左移
            elif direction == 3 and x == top:  # 向上，到上边界
                direction = 0
                top -= 1  # 上边界上移
            x += directions[direction][0]
            y += directions[direction][1]

        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.spiralMatrixIII(1, 4, 0, 0))  # [[0, 0], [0, 1], [0, 2], [0, 3]]
