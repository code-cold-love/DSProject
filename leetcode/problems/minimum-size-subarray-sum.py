#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 209. 长度最小的子数组 https://leetcode.cn/problems/minimum-size-subarray-sum/
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 找出 nums 中和 >= target 的长度最小的连续子数组，并返回其长度
        l = len(nums)
        left = right = 0
        min_len = float('inf')  # 窗口最小长度
        cur_sum = 0  # 当前窗口内的类加值

        while right < l:
            cur_sum += nums[right]
            while cur_sum >= target:
                min_len = min(min_len, right - left + 1)
                cur_sum -= nums[left]
                left += 1
            right += 1
        return min_len if min_len != float('inf') else 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.minSubArrayLen(4, [1, 4, 4]))  # 1
    print(solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))  # 2
