#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 54. 螺旋矩阵 https://leetcode.cn/problems/spiral-matrix/
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        ret = []
        if not rows or not cols:
            return ret
        elif rows == 1:
            ret = matrix[0]
        elif cols == 1:
            for i in range(rows):
                ret.append(matrix[i][0])
        else:
            upper, lower = 0, rows - 1
            left, right = 0, cols - 1
            while True:
                for j in range(left, right + 1):  # 从左到右
                    ret.append(matrix[upper][j])
                upper += 1
                if upper > lower:
                    break

                for i in range(upper, lower + 1):  # 从上到下
                    ret.append(matrix[i][right])
                right -= 1
                if right < left:
                    break

                for j in range(right, left - 1, -1):  # 从右到左
                    ret.append(matrix[lower][j])
                lower -= 1
                if lower < upper:
                    break

                for i in range(lower, upper - 1, -1):  # 从下到上
                    ret.append(matrix[i][left])
                left += 1
                if left > right:
                    break
        return ret


if __name__ == '__main__':
    obj = Solution()
    print(obj.spiralOrder([[1]]))  # [1]
    print(obj.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # [1, 2, 3, 6, 9, 8, 7, 4, 5]
