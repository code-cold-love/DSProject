#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 3290. 最高乘法得分 https://leetcode.cn/problems/maximum-multiplication-score/
from functools import cache
from math import inf
from typing import List


class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        # len(a) == 4, 4 <= len(b) <= 10**5
        # 【选或不选】动态规划
        @cache
        def dfs(i: int, j: int) -> int:
            """
            记忆化搜索
            :param i: 从右向左遍历数组 b 的下标
            :param j: 从 b[0] 到 b[i] 选 j+1 个数，与 a[0] 到 a[j] 计算点积
            :return:
            """
            if j < 0:  # b 中选完了四个数
                return 0
            if i < 0:  # 此时 j >= 0，没选完
                return -inf  # 表示不合法的状态

            # dfs(i - 1, j) 表示不选
            # dfs(i - 1, j - 1) + b[i] * a[j] 表示选
            return max(dfs(i - 1, j), dfs(i - 1, j - 1) + b[i] * a[j])

        ans = dfs(len(b) - 1, 3)
        dfs.cache_clear()  # 防止爆内存
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxScore([-1, 4, 5, -2], [-5, -1, -3, -2, -4]))  # -1
    print(solution.maxScore([3, 2, 5, 6], [2, -6, 4, -5, -3, 2, -7]))  # 26
