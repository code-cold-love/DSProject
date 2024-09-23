#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1014. 最佳观光组合 https://leetcode.cn/problems/best-sightseeing-pair/
from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = 0
        max_i = values[0] + 0
        # values[i] + values[j] + i - j = (values[i] + i) + (values[j] - j)
        # 在遍历 j 的情况下，求最佳观光组合等价于求 [0, j-1] 中 (values[i] + i) 的最大值
        for j in range(1, len(values)):
            ans = max(ans, max_i + values[j] - j)
            max_i = max(max_i, values[j] + j)
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxScoreSightseeingPair([1, 2]))  # 2
    print(solution.maxScoreSightseeingPair([8, 1, 5, 2, 6]))  # 11
