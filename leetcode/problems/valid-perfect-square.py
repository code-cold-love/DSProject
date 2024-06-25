#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 367. 有效的完全平方数 https://leetcode.cn/problems/valid-perfect-square/
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # 牛顿迭代法
        x0 = num
        while True:
            x1 = (x0 + num / x0) / 2
            if x0 - x1 < 1e-6:
                break
            x0 = x1
        x0 = int(x0)
        return x0 * x0 == num


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPerfectSquare(14))  # False
    print(solution.isPerfectSquare(16))  # True
