#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 131. 分割回文串 https://leetcode.cn/problems/palindrome-partitioning/
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        f = [[True] * n for _ in range(n)]  # 动态规划

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = (s[i] == s[j]) and f[i + 1][j - 1]

        ret, temp = list(), list()

        def backtrack(x: int):
            if x == n:
                ret.append(temp[:])
                return
            for y in range(x, n):
                if f[x][y]:
                    temp.append(s[x:y + 1])
                    backtrack(y + 1)
                    temp.pop()

        backtrack(0)
        return ret


if __name__ == '__main__':
    obj = Solution()
    print(obj.partition('a'))  # [['a']]
    print(obj.partition('aab'))  # [['a', 'a', 'b'], ['aa', 'b']]
