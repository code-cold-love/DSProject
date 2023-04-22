# -*- coding: utf-8 -*-
# 2352. 相等行列对 https://leetcode.cn/problems/equal-row-and-column-pairs/
from typing import List
from collections import Counter


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        counter = Counter(tuple(row) for row in grid)
        return sum(counter[col] for col in zip(*grid))  # zip(*args) 反压缩


if __name__ == '__main__':
    obj = Solution()
    print(obj.equalPairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]]))  # 1
