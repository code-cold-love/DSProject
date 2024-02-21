#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 189. 轮转数组 https://leetcode.cn/problems/rotate-array/
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n  # k < n
        nums[:] = nums[n - k:] + nums[:n - k]


if __name__ == '__main__':
    obj = Solution()
    arr = [1, 2, 3, 4, 5, 6, 7]
    obj.rotate(arr, k=3)
    print(arr)  # [5, 6, 7, 1, 2, 3, 4]
