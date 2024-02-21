#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 746. 使用最小花费爬楼梯 https://leetcode.cn/problems/min-cost-climbing-stairs/
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 2)  # dp[i] 表示从下标为 i 的台阶爬到顶层所需要的最小花费
        for i in range(n - 1, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
        return min(dp[0], dp[1])

    def minCostClimbingStairs_opt(self, cost: List[int]) -> int:
        # 双指针优化空间
        n = len(cost)
        cur = pre_1 = 0
        for i in range(n - 1, -1, -1):
            pre_2 = pre_1
            pre_1 = cur
            cur = cost[i] + min(pre_1, pre_2)
        return min(cur, pre_1)


if __name__ == '__main__':
    obj = Solution()
    print(obj.minCostClimbingStairs([10, 15, 20]))  # 15
    print(obj.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # 6
    print(obj.minCostClimbingStairs_opt([10, 15, 20]))  # 15
    print(obj.minCostClimbingStairs_opt([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # 6
