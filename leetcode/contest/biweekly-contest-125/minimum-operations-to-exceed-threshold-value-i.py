#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 3065. 超过阈值的最少操作数 I https://leetcode.cn/problems/minimum-operations-to-exceed-threshold-value-i/
from typing import List
from bisect import bisect_left


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        return bisect_left(nums, k)


if __name__ == '__main__':
    obj = Solution()
    print(obj.minOperations([1, 1, 2, 4, 9], 1))  # 0
    print(obj.minOperations([1, 1, 2, 4, 9], 9))  # 4
    print(obj.minOperations([2, 11, 10, 1, 3], 10))  # 3
