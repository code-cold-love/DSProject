#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2961. 双模幂运算 https://leetcode.cn/problems/double-modular-exponentiation/
from typing import List


class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        # variables[i] = [ai, bi, ci, mi]
        def calculate(a: int, b: int, c: int, m: int) -> int:
            # pow(x, y, z) >> (x ^ y) % z
            return pow(pow(a, b, 10), c, m)

        ans = []
        for i, var in enumerate(variables):
            if calculate(var[0], var[1], var[2], var[3]) == target:
                ans.append(i)
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.getGoodIndices([[2, 3, 3, 10], [3, 3, 3, 1], [6, 1, 1, 4]], 2))  # [0, 2]
