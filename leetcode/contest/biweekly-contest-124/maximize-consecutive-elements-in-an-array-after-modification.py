#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 3041. 修改数组后最大化数组中的连续元素数目 https://leetcode.cn/problems/maximize-consecutive-elements-in-an-array-after-modification/
from collections import defaultdict
from typing import List


class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        # dp[i][x] 表示前 i 个元素以数字 x 为结尾的连续子序列的最大长度
        # dp[i][x] = dp[i - 1][x - 1] + 1
        # 第 i 位要继承第 i - 1 位的全部状态，所以可把第一维优化掉
        dp = defaultdict(int)  # dp[x] 表示子序列最后一个数是 x 时，连续子序列的最大长度
        for num in nums:
            dp[num + 1] = max(dp[num + 1], dp[num] + 1)  # 操作，x+1 可以接在末尾为 x 的子序列后面
            dp[num] = max(dp[num], dp[num - 1] + 1)  # 不操作，x 可以接在末尾为 x-1 的子序列后面
        return max(dp.values())


if __name__ == '__main__':
    obj = Solution()
    print(obj.maxSelectedElements([1, 4, 7, 10]))  # 1
    print(obj.maxSelectedElements([2, 1, 5, 1, 1]))  # 3
