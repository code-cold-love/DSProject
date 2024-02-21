#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 45. 跳跃游戏 II https://leetcode.cn/problems/jump-game-ii/
from sys import maxsize
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # 生成的测试用例可以到达 nums[n - 1]
        n = len(nums)
        dp = [maxsize for _ in range(n)]
        dp[0] = 0
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if nums[j] + j >= i:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1]

    def jump_opt(self, nums: List[int]) -> int:
        # 贪心，正向查找可到达的最大位置
        n = len(nums)
        right_most = end = step = 0  # 向右最远可以到达的位置
        for i in range(n - 1):
            if right_most >= i:
                right_most = max(right_most, i + nums[i])
                if i == end:
                    end = right_most
                    step += 1
        return step


if __name__ == '__main__':
    obj = Solution()
    print(obj.jump_opt([2, 3, 1, 1, 4]))  # 2
    print(obj.jump_opt([2, 3, 0, 1, 4]))  # 2
