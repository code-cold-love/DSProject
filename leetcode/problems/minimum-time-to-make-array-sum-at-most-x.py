#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2809. 使数组和小于等于 x 的最少时间 https://leetcode.cn/problems/minimum-time-to-make-array-sum-at-most-x/
from typing import List


class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        pairs = sorted(zip(nums1, nums2), key=lambda p: p[1])
        n = len(pairs)
        f = [0] * (n + 1)
        for i, (a, b) in enumerate(pairs):
            for j in range(i + 1, 0, -1):
                f[j] = max(f[j], f[j - 1] + a + b * j)

        s1 = sum(nums1)
        s2 = sum(nums2)
        for t, v in enumerate(f):
            if s1 + s2 * t - v <= x:
                return t
        return -1


if __name__ == '__main__':
    obj = Solution()
    print(obj.minimumTime([1, 2, 3], [1, 2, 3], 4))  # 3
    print(obj.minimumTime([1, 2, 3], [3, 3, 3], 4))  # -1
