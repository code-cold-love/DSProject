#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 100220. 相同分数的最大操作数目 II https://leetcode.cn/contest/biweekly-contest-124/problems/maximum-number-of-operations-with-the-same-score-ii/
from typing import List
from executing import cache


class Solution:
    def maxOperations(self, A: List[int]) -> int:
        # 动态规划、深度优先搜索
        @cache
        def dp(i, j, v):
            if i >= j: return 0
            res = 0
            if A[i] + A[i + 1] == v:
                res = max(res, dp(i + 2, j, v) + 1)
            if A[i] + A[j] == v:
                res = max(res, dp(i + 1, j - 1, v) + 1)
            if A[j] + A[j - 1] ==v:
                res = max(res, dp(i, j - 2, v) + 1)
            return res

        ans = 0
        ans = max(ans, dp(0, len(A) - 1, A[0] + A[1]))
        ans = max(ans, dp(0, len(A) - 1, A[0] + A[-1]))
        ans = max(ans, dp(0, len(A) - 1, A[-1] + A[-2]))
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.maxOperations([3, 2, 6, 1, 4]))  # 2
    print(obj.maxOperations([3, 2, 1, 2, 3, 4]))  # 3
