#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 3011. 判断一个数组是否可以变为有序 https://leetcode.cn/problems/find-if-array-can-be-sorted/
from itertools import pairwise
from typing import List


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        # 分组循环，nums 全是正整数组成
        i, n = 0, len(nums)
        while i < n:  # 外层循环遍历组之前的准备工作（记录开始位置）
            start = i
            ones = nums[start].bit_count()
            i += 1
            while i < n and nums[i].bit_count() == ones:
                i += 1  # 内层循环遍历组，找出这一组最远在哪结束
            nums[start: i] = sorted(nums[start: i])
        return all(x <= y for x, y in pairwise(nums))


if __name__ == '__main__':
    solution = Solution()
    print(solution.canSortArray([3, 16, 8, 4, 2]))  # False
    print(solution.canSortArray([8, 4, 2, 30, 15]))  # True
