# -*- coding: utf-8 -*-
# 77. 组合 https://leetcode.cn/problems/combinations/
from typing import List
from itertools import combinations


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        elif k == 1:
            return [[i] for i in range(1, n + 1)]
        return list(combinations(range(1, n + 1), k))


if __name__ == '__main__':
    obj = Solution()
    print(obj.combine(1, 1))  # [[1]]
    print(obj.combine(4, 2))
