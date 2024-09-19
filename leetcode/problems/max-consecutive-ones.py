#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 485. 最大连续 1 的个数 https://leetcode.cn/problems/max-consecutive-ones/
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        i, n = 0, len(nums)
        while i < n:
            if nums[i] == 0:
                i += 1
                continue
            tmp = 0
            while i < n and nums[i] == 1:
                i += 1
                tmp += 1
            ans = max(ans, tmp)
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))  # 2
    print(solution.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))  # 3
