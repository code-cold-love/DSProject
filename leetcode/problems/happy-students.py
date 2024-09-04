#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2860. 让所有学生保持开心的分组方法数 https://leetcode.cn/problems/happy-students/
from typing import List


class Solution:
    def countWays(self, nums: List[int]) -> int:
        # 0 <= nums[i] < len(nums)
        # 在选择学生人数固定的时候，选择方案是唯一的
        nums.sort()  # 非递减排序
        n = len(nums)
        ans = nums[0] > 0  # 此时可以一个学生都不选
        for i in range(1, n):  # 枚举被选中的学生数
            if nums[i - 1] < i < nums[i]:
                ans += 1
        return ans + 1  # 数据范围保证 nums[i] < n，一定可以都选


if __name__ == '__main__':
    solution = Solution()
    print(solution.countWays([1, 1]))  # 2
    print(solution.countWays([6, 0, 3, 3, 6, 7, 2, 7]))  # 3
