#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 3194. 最小元素和最大元素的最小平均值 https://leetcode.cn/problems/minimum-average-of-smallest-and-largest-elements/
from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        n = len(nums)  # n 为偶数
        return min(nums[i] + nums[-1-i] for i in range(n // 2)) / 2


if __name__ == '__main__':
    solution = Solution()
    print(solution.minimumAverage(nums=[1, 2, 3, 7, 8, 9]))  # 5.0
