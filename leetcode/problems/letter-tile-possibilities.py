# -*- coding: utf-8 -*-
# 1079. 活字印刷 https://leetcode.cn/problems/letter-tile-possibilities/
from math import comb
from collections import Counter


class Solution:
    def numTilePossibilities(self, ts):
        # code from min time
        dp, cv, allen = [1] + [0] * len(ts), Counter(ts).values(), 0
        for v in cv:
            allen += v
            for i in range(allen, 0, -1):
                dp[i] += sum(dp[i - j] * comb(i, j) for j in range(1, min(i, v) + 1))
        return sum(dp) - 1


if __name__ == '__main__':
    obj = Solution()
    print(obj.numTilePossibilities('AAB'))  # 8
