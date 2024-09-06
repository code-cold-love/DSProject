#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 300. 最长递增子序列 https://leetcode.cn/problems/longest-increasing-subsequence/
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 1 <= nums.length <= 2500
        n = len(nums)
        dp = [1] * n  # dp[i] 是以 nums[i] 结尾的最长序列长度，必须包含 nums[i]
        for i in range(n):
            for j in range(i):  # 遍历 [0, i)
                if nums[j] < nums[i]:  # 满足严格递增的情况
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLIS([0, 1, 0, 3, 2, 3]))  # 4
    print(solution.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))  # 1
