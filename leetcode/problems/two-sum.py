#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1. 两数之和 https://leetcode.cn/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):  # 从前往后
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([3, 3], 6))  # [0, 1]
    print(solution.twoSum([3, 2, 4], 6))  # [1, 2]
    print(solution.twoSum([2, 7, 11, 15], 9))  # [0, 1]
