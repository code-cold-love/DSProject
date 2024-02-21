#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1043. 分隔数组以得到最大和 https://leetcode.cn/problems/partition-array-for-maximum-sum/
from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # 1 <= k <= len(arr) <= 500
        n = len(arr)
        dp = [0] * (n + 1)  # dp[i] 为以 i 结尾分割的最大和
        for i in range(1, n + 1):
            max_value = arr[i - 1]
            for j in range(i - 1, max(-1, i - k - 1), -1):
                dp[i] = max(dp[i], dp[j] + max_value * (i - j))
                if j > 0:
                    max_value = max(max_value, arr[j - 1])
        return dp[n]


if __name__ == '__main__':
    obj = Solution()
    print(obj.maxSumAfterPartitioning([1, 15, 7, 9, 2, 5, 10], k=3))  # 84
    print(obj.maxSumAfterPartitioning([1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], k=4))  # 83
