#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 977. 有序数组的平方 https://leetcode.cn/problems/squares-of-a-sorted-array/
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(i * i for i in nums)


if __name__ == '__main__':
    obj = Solution()
    print(obj.sortedSquares([-4, -1, 0, 3, 10]))  # [0, 1, 9, 16, 100]
