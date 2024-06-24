#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 503. 下一个更大元素 II https://leetcode.cn/problems/next-greater-element-ii/
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # 单调栈，其中保存的是 nums 下标
        n = len(nums)
        ans = [-1] * n
        stk = list()
        for i in range(n * 2 - 1):  # 只遍历一次序列是不够的，把数组“拉直”，多循环遍历一遍
            while stk and nums[stk[-1]] < nums[i % n]:
                ans[stk.pop()] = nums[i % n]
            stk.append(i % n)

        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.nextGreaterElements([1, 2, 1]))  # [2, -1, 2]
    print(solution.nextGreaterElements([1, 2, 3, 4, 3]))  # [2, 3, 4, -1, 4]
