#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 718. 最长重复子数组 https://leetcode.cn/problems/maximum-length-of-repeated-subarray/
from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """返回两个数组中公共的、长度最长的子数组的长度"""
        # 1 <= nums1.length, nums2.length <= 1000
        ans = 0
        m, n = len(nums1), len(nums2)
        # dp[i][j] 为 nums1[i:] 与 nums2[j:] 的最长公共前缀
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # 当 nums1[i] == nums2[j] 时，dp[i][j] 为 nums1[i+1] 与 nums2[j+1] 的最长公共前缀再加 1
                dp[i][j] = dp[i + 1][j + 1] + 1 if nums1[i] == nums2[j] else 0
                ans = max(ans, dp[i][j])
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.findLength([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]))  # 5
    print(solution.findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))  # 3
