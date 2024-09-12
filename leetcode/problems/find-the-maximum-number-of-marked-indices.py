#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2576. 求出最多标记下标 https://leetcode.cn/problems/find-the-maximum-number-of-marked-indices/
from typing import List


class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        # 枚举可以匹配的对数 k，二分法
        nums.sort()
        left, right = 0, len(nums) // 2 + 1  # 开区间
        while left + 1 < right:
            k = (left + right) // 2
            if all(nums[i] * 2 <= nums[i - k] for i in range(k)):
                left = k
            else:
                right = k
        return left * 2  # 最多匹配 left 对，有 left * 2 个数


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxNumOfMarkedIndices([7, 6, 8]))  # 0
    print(solution.maxNumOfMarkedIndices([3, 5, 2, 4]))  # 2
    print(solution.maxNumOfMarkedIndices([9, 2, 5, 4]))  # 4
