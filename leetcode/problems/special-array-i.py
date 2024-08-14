#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 3151. 特殊数组 I https://leetcode.cn/problems/special-array-i/
from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(1, n):
            if nums[i - 1] % 2 == nums[i] % 2:  # 判断前后奇偶性
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isArraySpecial([1]))  # True
    print(solution.isArraySpecial([2, 1, 4]))  # True
