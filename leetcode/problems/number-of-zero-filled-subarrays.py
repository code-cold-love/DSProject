#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2348. 全 0 子数组的数目 https://leetcode.cn/problems/number-of-zero-filled-subarrays/
from typing import List


class Solution:
    @staticmethod
    def calculate(x: int) -> int:
        return x * (x + 1) >> 1

    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        i, n = 0, len(nums)
        while i < n:
            if nums[i] != 0:
                i += 1
                continue
            tmp = 0
            while i < n and nums[i] == 0:
                i += 1
                tmp += 1
            ans += self.calculate(tmp)
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.zeroFilledSubarray([2, 10, 2019]))  # 0
    print(solution.zeroFilledSubarray([0, 0, 0, 2, 0, 0]))  # 9
    print(solution.zeroFilledSubarray([1, 3, 0, 0, 2, 0, 0, 4]))  # 6
