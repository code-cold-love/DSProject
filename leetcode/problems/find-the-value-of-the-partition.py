#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2740. 找出分区值 https://leetcode.cn/problems/find-the-value-of-the-partition/
from itertools import pairwise
from typing import List


class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        # 2 <= nums.length <= 10**5
        # 分区值 abs(max(nums1) - min(nums2))
        nums.sort()
        return min(y - x for x, y in pairwise(nums))


if __name__ == '__main__':
    solution = Solution()
    print(solution.findValueOfPartition([100, 1, 10]))  # 9
    print(solution.findValueOfPartition([1, 3, 2, 4]))  # 1
    print(solution.findValueOfPartition(
        [771963616, 776813785, 28603508, 639757365, 958320601, 988875230, 197812712, 27130325, 844013034,
         334036196]))  # 1473183
