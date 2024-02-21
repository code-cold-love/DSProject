#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 167. 两数之和 II - 输入有序数组 https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # nums 按非递减顺序排列，仅存在一个有效答案
        left, right = 0, len(numbers) - 1
        while left < right:
            val = numbers[left] + numbers[right]
            if val == target:
                return [left + 1, right + 1]
            elif val > target:
                right -= 1
            else:
                left += 1
        return [-1, -1]


if __name__ == '__main__':
    obj = Solution()
    print(obj.twoSum([2, 7, 11, 15], 9))  # [1, 2]
