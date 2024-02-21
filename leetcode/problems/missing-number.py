#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 268. 丢失的数字 https://leetcode.cn/problems/missing-number/
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """哈希"""
        n, s = 0, set()
        for num in nums:
            n += 1
            s.add(num)
        for i in range(n + 1):
            if i not in s:
                return i

    def missingNumber_bit(self, nums: List[int]) -> int:
        """位运算"""
        xor = 0
        for i, num in enumerate(nums):
            xor ^= i ^ num
        return xor ^ len(nums)


if __name__ == '__main__':
    obj = Solution()
    print(obj.missingNumber([3, 0, 1]))  # 2
    print(obj.missingNumber_bit([3, 0, 1]))  # 2
