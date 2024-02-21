#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2670. 找出不同元素数目差数组 https://leetcode.cn/problems/find-the-distinct-difference-array/
from typing import List



class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        hash_set = set()
        suffix = [0] * (n + 1)
        for i in range(n - 1, 0, -1):
            hash_set.add(nums[i])
            suffix[i] = len(hash_set)
        hash_set.clear()
        diff = [0] * n
        for i in range(n):
            hash_set.add(nums[i])
            diff[i] = len(hash_set) - suffix[i + 1]
        return diff


if __name__ == '__main__':
    obj = Solution()
    print(obj.distinctDifferenceArray([1, 2, 3, 4, 5]))  # [-3, -1, 1, 3, 5]
    print(obj.distinctDifferenceArray([3, 2, 3, 4, 2]))  # [-2, -1, 0, 2, 3]
