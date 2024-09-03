#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 152. 乘积最大子数组 https://leetcode.cn/problems/maximum-product-subarray/
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_f, min_f, ans = nums[0], nums[0], nums[0]
        for x in nums[1:]:
            mx, mn = max_f, min_f
            # 注意：本题要求【非空连续子数组】的最大乘积
            # 与 max_f = max(mx, x, mn * x, mx * x) 相区别
            max_f = max(x, mn * x, mx * x)
            min_f = min(x, mn * x, mx * x)
            ans = max(max_f, ans)
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProduct([-2, 0, -1]))  # 0
    print(solution.maxProduct([2, 3, -2, 4]))  # 6
