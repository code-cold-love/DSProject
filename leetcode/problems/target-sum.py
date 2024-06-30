#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 494. 目标和 https://leetcode.cn/problems/target-sum/
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # nums 非负整数数组
        # total 为数组的元素和，neg 为添加 - 号的元素绝对值之和，pos 为添加 + 号的元素之和
        # total = neg + pos -> pos = total - neg
        # pos - neg = target -> target = total - 2 * neg
        # neg = (total - target) / 2
        # 因为 nums 为非负整数数组，所以 neg 也必须是非负整数，所以 (total - target) 为非负偶数，否则不存在满足 target 的情况
        total = sum(nums)
        diff = total - target
        if diff < 0 or diff % 2 != 0:
            return 0
        neg = diff >> 1
        dp = [0] * (neg + 1)
        dp[0] = 1
        for x in nums:
            for i in range(neg, x - 1, -1):
                dp[i] += dp[i - x]
        return dp[neg]


if __name__ == '__main__':
    solution = Solution()
    print(solution.findTargetSumWays([1], 1))  # 1
    print(solution.findTargetSumWays([1, 1, 1, 1, 1], 3))  # 5
