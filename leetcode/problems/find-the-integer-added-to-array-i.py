#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 3131. 找出与数组相加的整数 I https://leetcode.cn/problems/find-the-integer-added-to-array-i/
from typing import List


class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        return min(nums2) - min(nums1)


if __name__ == '__main__':
    solution = Solution()
    print(solution.addedInteger([10], [5]))  # -5
    print(solution.addedInteger([2, 6, 4], [9, 7, 5]))  # 3
