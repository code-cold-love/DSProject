#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1641. 统计字典序元音字符串的数目 https://leetcode.cn/problems/count-sorted-vowel-strings/
from math import comb


class Solution:
    def countVowelStrings(self, n: int) -> int:
        # 元音 a e i o u；1 <= n <= 50
        # dp[i][j] 表示长度为 i + 1，以 j 结尾的按字典序排列的字符串数量
        dp = [1] * 5
        for _ in range(n - 1):
            for j in range(1, 5):
                dp[j] += dp[j - 1]
        return sum(dp)

    def countVowelStrings_math(self, n: int) -> int:
        return comb(n + 4, 4)


if __name__ == '__main__':
    obj = Solution()
    print(obj.countVowelStrings(1))  # 5
    print(obj.countVowelStrings(2))  # 15
    print(obj.countVowelStrings(3))  # 35
    print(obj.countVowelStrings(33))  # 66045
