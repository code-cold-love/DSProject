#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 3176. 求出最长好子序列 I https://leetcode.cn/problems/find-the-maximum-length-of-a-good-subsequence-i/
from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        # 0 <= k <= min(nums.length, 25)
        n, ans = len(nums), 0
        # dp[i][j] 表示以 nums[i] 为结尾的序列中至多有 j 个数字与其在序列中的后一个数字不相等
        dp = [[-1 for _ in range(k + 1)] for _ in range(n)]
        for i in range(n):
            dp[i][0] = 1
            for tmp_k in range(k + 1):
                for tmp_i in range(i):
                    add = 1 if nums[i] != nums[tmp_i] else 0
                    if tmp_k - add >= 0 and dp[tmp_i][tmp_k - add] != -1:
                        # l-add >= 0 表示不相等对数没超过限制
                        dp[i][tmp_k] = max(dp[i][tmp_k], dp[tmp_i][tmp_k - add] + 1)
                ans = max(ans, dp[i][tmp_k])
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.maximumLength([1, 2, 1, 1, 3], 2))  # 4
    print(solution.maximumLength([1, 2, 3, 4, 5, 1], 0))  # 2
