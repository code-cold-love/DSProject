#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 34. 在排序数组中查找元素的第一个和最后一个位置 https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/
from typing import List
from bisect import bisect_left, bisect_right


class Solution:
    @staticmethod
    def process_left(n: int, nums: List[int], target: int, pivot: int) -> int:
        if pivot < n and nums[pivot] == target:
            return pivot
        return -1

    @staticmethod
    def process_right(n: int, nums: List[int], target: int, pivot: int) -> int:
        if 0 < pivot <= n and nums[pivot - 1] == target:
            return pivot - 1
        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # nums 非递减排序
        n = len(nums)
        left, right = bisect_left(nums, target), bisect_right(nums, target)
        return [self.process_left(n, nums, target, left), self.process_right(n, nums, target, right)]


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchRange([1], 1))  # [0, 0]
    print(solution.searchRange([], 0))  # [-1, -1]
    print(solution.searchRange([5, 7, 7, 8, 8, 10], 8))  # [3, 4]
    print(solution.searchRange([5, 7, 7, 8, 8, 10], 6))  # [-1, -1]
