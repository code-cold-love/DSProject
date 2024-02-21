#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1031. 两个非重叠子数组的最大和 https://leetcode.cn/problems/maximum-sum-of-two-non-overlapping-subarrays/
from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        return max(self.help(nums, firstLen, secondLen), self.help(nums, secondLen, firstLen))

    @staticmethod
    def help(nums: list, first_len: int, second_len: int):
        sum_left = sum_right = 0
        for i in range(0, first_len):
            sum_left += nums[i]
        max_left = sum_left
        for i in range(first_len, first_len + second_len):
            sum_right += nums[i]
        res = max_left + sum_right
        j = first_len
        for i in range(first_len + second_len, len(nums)):  # i - j = second_len
            sum_left += nums[j] - nums[j - first_len]
            max_left = max(max_left, sum_left)
            sum_right += nums[i] - nums[i - second_len]
            res = max(res, max_left + sum_right)
            j += 1
        return res


if __name__ == '__main__':
    obj = Solution()
    print(obj.maxSumTwoNoOverlap([0, 6, 5, 2, 2, 5, 1, 9, 4], 1, 2))  # 20
