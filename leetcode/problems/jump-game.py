#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 55. 跳跃游戏 https://leetcode.cn/problems/jump-game/
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 动态规划
        n = len(nums)
        dp = [False] * n
        dp[0] = True
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if dp[j] and nums[j] >= i - j:
                    dp[i] = True
                    break
        return dp[-1]

    def canJump_opt(self, nums: List[int]) -> bool:
        # 贪心
        n = len(nums)
        right_most = 0  # 右边最远可以到达的位置
        for i in range(n):
            if i <= right_most:
                right_most = max(right_most, i + nums[i])
                if right_most >= n - 1:
                    return True
        return False


if __name__ == '__main__':
    obj = Solution()
    print(obj.canJump([2, 3, 1, 1, 4]))  # True
    print(obj.canJump([3, 2, 1, 0, 4]))  # False
    print(obj.canJump_opt([2, 3, 1, 1, 4]))  # True
    print(obj.canJump_opt([3, 2, 1, 0, 4]))  # False
