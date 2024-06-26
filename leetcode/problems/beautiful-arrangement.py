#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 526. 优美的排列 https://leetcode.cn/problems/beautiful-arrangement/
from functools import cache


class Solution:
    def countArrangement(self, n: int) -> int:
        f = [0] * (1 << n)  # << 左移，即乘 2 的幂

        @cache
        def dfs(s: int) -> int:  # s 表示可以选的数字集合
            if s == 0:
                return 1
            ans = 0
            i = s.bit_count()
            for j in range(1, n + 1):
                if s >> (j - 1) & 1 and (i % j == 0 or j % i == 0):
                    ans += dfs(s ^ (1 << (j - 1)))
            return ans

        return dfs((1 << n) - 1)


if __name__ == '__main__':
    solution = Solution()
    print(solution.countArrangement(2))  # 2
    print(solution.countArrangement(1))  # 1
