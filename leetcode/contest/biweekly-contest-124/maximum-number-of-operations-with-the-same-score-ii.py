#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 3040. 相同分数的最大操作数目 II https://leetcode.cn/problems/maximum-number-of-operations-with-the-same-score-ii/
from functools import cache
from typing import List


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        """动态规划 + 记忆化搜索"""
        n = len(nums)

        @cache
        def dp(start: int, end: int, target: int) -> int:
            if start >= end:
                return 0
            tmp_ans = 0
            if nums[start] + nums[start + 1] == target:
                tmp_ans = max(tmp_ans, 1 + dp(start + 2, end, target))
            if nums[start] + nums[end] == target:
                tmp_ans = max(tmp_ans, 1 + dp(start + 1, end - 1, target))
            if nums[end] + nums[end - 1] == target:
                tmp_ans = max(tmp_ans, 1 + dp(start, end - 2, target))
            return tmp_ans

        return max(dp(0, n - 1, nums[0] + nums[1]), dp(0, n - 1, nums[0] + nums[-1]), dp(0, n - 1, nums[-1] + nums[-2]))


if __name__ == '__main__':
    obj = Solution()
    print(obj.maxOperations([3, 2, 6, 1, 4]))  # 2
    print(obj.maxOperations([3, 2, 1, 2, 3, 4]))  # 3
