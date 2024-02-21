#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2012. 数组美丽值求和 https://leetcode.cn/problems/sum-of-beauty-in-the-array/
from typing import List


class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        # 前缀最大值，后缀最小值
        n = len(nums)
        flag = [0] * n
        pre_max, suf_min = nums[0], nums[-1]
        for i in range(1, n):  # 从前往后遍历，更新前缀最大值
            if nums[i] > pre_max:
                pre_max = nums[i]
                flag[i] += 1
        for i in range(n - 2, 0, -1):  # 从后往前遍历，更新后缀最小值
            if nums[i] < suf_min:
                suf_min = nums[i]
                flag[i] += 1
        ans = 0
        for i in range(1, n - 1):
            if nums[i - 1] < nums[i] < nums[i + 1]:
                ans += 1  # 满足条件 2
            if flag[i] == 2:
                ans += 1  # 满足条件 1
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.sumOfBeauties([1, 2, 3]))  # 2
    print(obj.sumOfBeauties([3, 2, 1]))  # 0
    print(obj.sumOfBeauties([2, 4, 6, 4]))  # 1
