#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 69. x 的平方根  https://leetcode.cn/problems/sqrtx/
from math import exp, log


class Solution:
    def mySqrt(self, x: int) -> int:
        # x 为非负整数
        if x == 0 or x == 1:
            return x
        ans = int(exp(0.5 * log(x)))
        return ans + 1 if (ans + 1) ** 2 <= x else ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.mySqrt(4))  # 2
    print(solution.mySqrt(8))  # 2
