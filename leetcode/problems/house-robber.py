#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 198. 打家劫舍 https://leetcode.cn/problems/house-robber/
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]

    def rob_1(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            first, second = second, max(first + nums[i], second)
        return second


if __name__ == '__main__':
    obj = Solution()
    print(obj.rob([1, 2, 3, 1]))  # 4
    print(obj.rob([2, 7, 9, 3, 1]))  # 12
