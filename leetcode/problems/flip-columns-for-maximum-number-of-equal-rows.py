#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1072. 按列翻转得到最大值等行数 https://leetcode.cn/problems/flip-columns-for-maximum-number-of-equal-rows/
from typing import List
from collections import Counter


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        count = Counter()
        for i, row in enumerate(matrix):
            value = 0
            for j, v in enumerate(row):
                value = value * 10 + (v ^ row[0])  # ^ 按位异或
            count[value] += 1
        return max(count.values())


if __name__ == '__main__':
    obj = Solution()
    print(obj.maxEqualRowsAfterFlips([[0, 0, 0], [0, 0, 1], [1, 1, 0]]))  # 2
