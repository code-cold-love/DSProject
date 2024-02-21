#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1033. 移动石子直到连续 https://leetcode.cn/problems/moving-stones-until-consecutive/
from typing import List


class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = sorted([a, b, c])
        minimum_moves = (b > a + 1) + (c > b + 1)
        if (c - b == 2 or b - a == 2) and minimum_moves > 1:
            minimum_moves = 1
        maximum_moves = c - a - 2
        return [minimum_moves, maximum_moves]


if __name__ == '__main__':
    obj = Solution()
    print(obj.numMovesStones(1, 2, 5))  # [1, 2]
    print(obj.numMovesStones(4, 3, 2))  # [0, 0]
    print(obj.numMovesStones(3, 5, 1))  # [1, 2]
