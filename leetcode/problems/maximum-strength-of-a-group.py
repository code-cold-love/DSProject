#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2708. 一个小组的最大实力值 https://leetcode.cn/problems/maximum-strength-of-a-group/
from typing import List


class Solution:
    def maxStrength_greedy(self, nums: List[int]) -> int:
        # 组成一个非空小组，且这个小组的实力值最大
        min_f = max_f = ans = nums[0]
        for x in nums[1:]:
            mx, mn = max_f, min_f
            max_f = max(mx, x, mn * x, mx * x)
            # 如果 x 是负数，min_ans * x 可以得到最大乘积
            min_f = min(mn, x, mn * x, mx * x)
            ans = max(max_f, ans)
        return ans

    def maxStrength(self, nums: List[int]) -> int:
        ans = 1
        neg = zero = pos = 0
        max_neg = -9  # 最大负数
        for num in nums:
            if num < 0:
                neg += 1
                ans *= num
                max_neg = max(max_neg, num)
            elif num == 0:
                zero += 1
            else:
                pos += 1
                ans *= num
        if neg == 1 and zero == 0 and pos == 0:
            return nums[0]
        elif neg <= 1 and pos == 0:  # 负数元素个数不能凑出一对，无正数
            return 0
        elif ans < 0:  # 有正数但乘积小于 0，此时除于最大负数以消去负号
            return ans // max_neg
        else:
            return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxStrength_greedy([-4, -5, -4]))  # 20
    print(solution.maxStrength([3, -1, -5, 2, 5, -9]))  # 1350
